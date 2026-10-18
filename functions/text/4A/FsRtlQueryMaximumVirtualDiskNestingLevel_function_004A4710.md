# FsRtlQueryMaximumVirtualDiskNestingLevel

- RVA: `0x004A4710`–`0x004A4732` (길이 `34` bytes)
- VA: `0x00000001404A4710`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082A88`
- 디코드: `10`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004A4725` → [FsRtlpGetMaxVirtualDiskNestingLevel](../58/FsRtlpGetMaxVirtualDiskNestingLevel_function_00582FDC.md) (function, `0x00582FDC`)

### Direct callers
- [FsRtlGetVirtualDiskNestingLevel](FsRtlGetVirtualDiskNestingLevel_function_004A4530.md) at `0x004A46AE`
- [FsRtlGetVirtualDiskNestingLevel](FsRtlGetVirtualDiskNestingLevel_function_004A4530.md) at `0x004A46BA`

### Static image references
- `0x004A4714` → RVA `0x00E0A8B8` (`.data`; read)
- `0x004A472A` → RVA `0x00E0A8B8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A4710  48 83 EC 28                     sub rsp, 0x28
004A4714  8B 05 9E 61 96 00               mov eax, dword ptr [rip + 0x96619e]
004A471A  83 F8 FF                        cmp eax, -1
004A471D  74 06                           je 0x1404a4725
004A471F  48 83 C4 28                     add rsp, 0x28
004A4723  C3                              ret
004A4724  CC                              int3
004A4725  E8 B2 E8 0D 00                  call 0x140582fdc
004A472A  89 05 88 61 96 00               mov dword ptr [rip + 0x966188], eax
004A4730  EB ED                           jmp 0x1404a471f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlQueryMaximumVirtualDiskNestingLevel(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9855390)))) == -1) goto loc_004A4725;
loc_004A471F:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(v_rip + 9855390));
loc_004A4725:
    result = FsRtlpGetMaxVirtualDiskNestingLevel(a1, a2, a3, a4);
    *(unsigned int *)(v_rip + 9855368) = (unsigned int)(result);
    goto loc_004A471F;
}
```

## 5. (Beta) C Style

```c
void FsRtlQueryMaximumVirtualDiskNestingLevel(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x96619E)))) == -1) goto loc_004A4725;
loc_004A471F:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(v_rip + 0x96619E));
loc_004A4725:
    result = FsRtlpGetMaxVirtualDiskNestingLevel(a1, a2, a3, a4);
    *(uint32_t *)(v_rip + 0x966188) = (uint32_t)(result);
    goto loc_004A471F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A4710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A4710[BB_004A4710]
  bb_004A471F[BB_004A471F]
  bb_004A4724[BB_004A4724]
  bb_004A4725[BB_004A4725]
  bb_004A4710 -->|branch| bb_004A4725
  bb_004A4710 -->|fallthrough| bb_004A471F
  bb_004A4724 -->|flow| bb_004A4725
  bb_004A4725 -->|branch| bb_004A471F
```
