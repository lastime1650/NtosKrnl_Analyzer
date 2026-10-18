# VfDriverInitSuccess

- RVA: `0x00B9A484`–`0x00B9A49D` (길이 `25` bytes)
- VA: `0x0000000140B9A484`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B9A492` → [ViDriverReApplyVerifierForAll](ViDriverReApplyVerifierForAll_function_00B9A8D4.md) (function, `0x00B9A8D4`)

### Direct callers
- [MiIssueDllInitializeCall](../../page/7F/MiIssueDllInitializeCall_function_007F8078.md) at `0x007F8125`
- [PnpInitializeBootStartDriver](../../init/C7/PnpInitializeBootStartDriver_function_00C760F0.md) at `0x00C76230`

### Static image references
- `0x00B9A48A` → RVA `0x00F048B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B9A484  48 83 EC 28                     sub rsp, 0x28
00B9A488  33 C0                           xor eax, eax
00B9A48A  39 0D 20 A4 36 00               cmp dword ptr [rip + 0x36a420], ecx
00B9A490  74 05                           je 0x140b9a497
00B9A492  E8 3D 04 00 00                  call 0x140b9a8d4
00B9A497  48 83 C4 28                     add rsp, 0x28
00B9A49B  C3                              ret
00B9A49C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfDriverInitSuccess(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if ((*(unsigned int *)(v_rip + 3580960)) != a1) {
        result = ViDriverReApplyVerifierForAll(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfDriverInitSuccess(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if ((*(uint32_t *)(v_rip + 0x36A420)) != Arg1) {
        result = ViDriverReApplyVerifierForAll(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9A484&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B9A484[BB_00B9A484]
  bb_00B9A492[BB_00B9A492]
  bb_00B9A497[BB_00B9A497]
  bb_00B9A49C[BB_00B9A49C]
  bb_00B9A484 -->|branch| bb_00B9A497
  bb_00B9A484 -->|fallthrough| bb_00B9A492
  bb_00B9A492 -->|flow| bb_00B9A497
```
