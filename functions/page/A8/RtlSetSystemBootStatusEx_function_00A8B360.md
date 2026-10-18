# RtlSetSystemBootStatusEx

- RVA: `0x00A8B360`–`0x00A8B37D` (길이 `29` bytes)
- VA: `0x0000000140A8B360`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A8B372` → [RtlpSystemBootStatusRequest](RtlpSystemBootStatusRequest_function_00A8B384.md) (function, `0x00A8B384`)

### Direct callers
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7F120`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8B360  48 83 EC 28                     sub rsp, 0x28
00A8B364  4D 8B C8                        mov r9, r8
00A8B367  44 8B C2                        mov r8d, edx
00A8B36A  48 8B D1                        mov rdx, rcx
00A8B36D  B9 20 00 00 00                  mov ecx, 0x20
00A8B372  E8 0D 00 00 00                  call 0x140a8b384
00A8B377  48 83 C4 28                     add rsp, 0x28
00A8B37B  C3                              ret
00A8B37C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlSetSystemBootStatusEx(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RtlpSystemBootStatusRequest(32, a1, (unsigned int)(a2), a3);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlSetSystemBootStatusEx(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RtlpSystemBootStatusRequest(32, Arg1, (uint32_t)(Arg2), Arg3);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8B360&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8B360[BB_00A8B360]
  bb_00A8B37C[BB_00A8B37C]
```
