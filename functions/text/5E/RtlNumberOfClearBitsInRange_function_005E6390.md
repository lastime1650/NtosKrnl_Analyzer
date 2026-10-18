# RtlNumberOfClearBitsInRange

- RVA: `0x005E6390`–`0x005E63B1` (길이 `33` bytes)
- VA: `0x00000001405E6390`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005E6399` → [RtlNumberOfSetBitsInRange](../4C/RtlNumberOfSetBitsInRange_function_004C7300.md) (function, `0x004C7300`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E6390  40 53                           push rbx
005E6392  48 83 EC 20                     sub rsp, 0x20
005E6396  41 8B D8                        mov ebx, r8d
005E6399  E8 62 0F EE FF                  call 0x1404c7300
005E639E  2B D8                           sub ebx, eax
005E63A0  83 C9 FF                        or ecx, 0xffffffff
005E63A3  3B C1                           cmp eax, ecx
005E63A5  0F 44 D9                        cmove ebx, ecx
005E63A8  8B C3                           mov eax, ebx
005E63AA  48 83 C4 20                     add rsp, 0x20
005E63AE  5B                              pop rbx
005E63AF  C3                              ret
005E63B0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlNumberOfClearBitsInRange(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = RtlNumberOfSetBitsInRange(a1, a2, a3, a4);
    v_rbx = (unsigned int)(((unsigned int)(a3)) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) == a1) { v_rbx = a1; }
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t RtlNumberOfClearBitsInRange(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = RtlNumberOfSetBitsInRange(Arg1, Arg2, Arg3, a4);
    local_rbx = (uint32_t)(((uint32_t)(Arg3)) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) == Arg1) { local_rbx = Arg1; }
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E6390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E6390[BB_005E6390]
  bb_005E63B0[BB_005E63B0]
```
