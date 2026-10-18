# RtlpHpSegVsAllocate

- RVA: `0x002EB320`–`0x002EB33D` (길이 `29` bytes)
- VA: `0x00000001402EB320`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `8`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002EB332` → [RtlpHpSegSubAllocate](RtlpHpSegSubAllocate_function_002EB344.md) (function, `0x002EB344`)

### Direct callers
- [RtlpHpVsSubsegmentCreate](RtlpHpVsSubsegmentCreate_function_002EAE30.md) at `0x002EAEBE`
- [RtlpHpLfhSubsegmentCreate](RtlpHpLfhSubsegmentCreate_function_002EC5A0.md) at `0x002EC683`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002EB320  48 83 EC 38                     sub rsp, 0x38
002EB324  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
002EB329  4D 8B C8                        mov r9, r8
002EB32C  41 B8 00 00 00 0C               mov r8d, 0xc000000
002EB332  E8 0D 00 00 00                  call 0x1402eb344
002EB337  48 83 C4 38                     add rsp, 0x38
002EB33B  C3                              ret
002EB33C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpSegVsAllocate(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = a4;
    result = RtlpHpSegSubAllocate(a1, a2, (unsigned int)(0xC000000ULL), a3);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpSegVsAllocate(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = Arg4;
    result = RtlpHpSegSubAllocate(Arg1, Arg2, (uint32_t)(0xC000000ULL), Arg3);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002EB320&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002EB320[BB_002EB320]
  bb_002EB33C[BB_002EB33C]
```
