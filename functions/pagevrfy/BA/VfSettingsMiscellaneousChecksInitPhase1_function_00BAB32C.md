# VfSettingsMiscellaneousChecksInitPhase1

- RVA: `0x00BAB32C`–`0x00BAB358` (길이 `44` bytes)
- VA: `0x0000000140BAB32C`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00BAB34D` → [ViSettingsEnableKernelHandleChecking](ViSettingsEnableKernelHandleChecking_function_00BAB360.md) (function, `0x00BAB360`)

### Direct callers
- [VfInitSystemNoRebootNeeded](../B9/VfInitSystemNoRebootNeeded_function_00B93970.md) at `0x00B93A74`
- [VerifierInitSystem](../../init/C4/VerifierInitSystem_function_00C4BC84.md) at `0x00C4BCC0`

### Static image references
- `0x00BAB330` → RVA `0x00F04A20` (`.data`; read)
- `0x00BAB33C` → RVA `0x00E681A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAB32C  48 83 EC 28                     sub rsp, 0x28
00BAB330  F7 05 E6 96 35 00 00 08 00 00   test dword ptr [rip + 0x3596e6], 0x800
00BAB33A  74 16                           je 0x140bab352
00BAB33C  F7 05 5A CE 2B 00 00 00 40 00   test dword ptr [rip + 0x2bce5a], 0x400000
00BAB346  75 0A                           jne 0x140bab352
00BAB348  B9 01 00 00 00                  mov ecx, 1
00BAB34D  E8 0E 00 00 00                  call 0x140bab360
00BAB352  48 83 C4 28                     add rsp, 0x28
00BAB356  C3                              ret
00BAB357  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfSettingsMiscellaneousChecksInitPhase1(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned int *)(v_rip + 3512038)) & (0x800ULL)) == 0) goto loc_00BAB352;
    if (((*(unsigned int *)(v_rip + 2870874)) & (0x400000ULL)) == 0) {
        a1 = 1;
        result = ViSettingsEnableKernelHandleChecking(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void VfSettingsMiscellaneousChecksInitPhase1(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint32_t *)(v_rip + 0x3596E6)) & (0x800ULL)) == 0) goto loc_00BAB352;
    if (((*(uint32_t *)(v_rip + 0x2BCE5A)) & (0x400000ULL)) == 0) {
        a1 = 1;
        result = ViSettingsEnableKernelHandleChecking(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAB32C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAB32C[BB_00BAB32C]
  bb_00BAB33C[BB_00BAB33C]
  bb_00BAB348[BB_00BAB348]
  bb_00BAB352[BB_00BAB352]
  bb_00BAB357[BB_00BAB357]
  bb_00BAB32C -->|branch| bb_00BAB352
  bb_00BAB32C -->|fallthrough| bb_00BAB33C
  bb_00BAB33C -->|branch| bb_00BAB352
  bb_00BAB33C -->|fallthrough| bb_00BAB348
  bb_00BAB348 -->|flow| bb_00BAB352
```
