# HalpBlkWdFatalExceptionCheck

- RVA: `0x0056E784`–`0x0056E7BF` (길이 `59` bytes)
- VA: `0x000000014056E784`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `16`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0056E7B3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [HalpBlkPoBusyWait](HalpBlkPoBusyWait_function_0056E128.md) at `0x0056E162`
- [HalpBlkWdWorkerRoutine](HalpBlkWdWorkerRoutine_function_0056E810.md) at `0x0056E828`

### Static image references
- `0x0056E788` → RVA `0x00F90550` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056E784  48 83 EC 38                     sub rsp, 0x38
0056E788  48 8B 05 C1 1D A2 00            mov rax, qword ptr [rip + 0xa21dc1]
0056E78F  44 8B C1                        mov r8d, ecx
0056E792  4A 8B 0C C0                     mov rcx, qword ptr [rax + r8*8]
0056E796  48 8B 41 78                     mov rax, qword ptr [rcx + 0x78]
0056E79A  48 85 C0                        test rax, rax
0056E79D  74 1A                           je 0x14056e7b9
0056E79F  44 0F B6 49 70                  movzx r9d, byte ptr [rcx + 0x70]
0056E7A4  BA 05 00 00 00                  mov edx, 5
0056E7A9  B9 DA 01 00 00                  mov ecx, 0x1da
0056E7AE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0056E7B3  E8 A8 EE F8 FF                  call 0x1404fd660
0056E7B8  CC                              int3
0056E7B9  48 83 C4 38                     add rsp, 0x38
0056E7BD  C3                              ret
0056E7BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpBlkWdFatalExceptionCheck(int a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10624449) + (unsigned int)(a1) * 8) + 120);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10624449) + (unsigned int)(a1) * 8) + 120) != 0) {
        a4 = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10624449) + (unsigned int)(a1) * 8) + 112);
        a2 = 5;
        a1 = 474;
        v_stack_m18 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10624449) + (unsigned int)(a1) * 8) + 120);
        result = KeBugCheckEx(a1, a2, (unsigned int)(a1), a4);
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpBlkWdFatalExceptionCheck(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA21DC1) + (uint32_t)(Arg1) * 8) + 0x78);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA21DC1) + (uint32_t)(Arg1) * 8) + 0x78) != 0) {
        a4 = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA21DC1) + (uint32_t)(Arg1) * 8) + 0x70);
        a2 = 5;
        Arg1 = 474;
        v_stack_m18 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA21DC1) + (uint32_t)(Arg1) * 8) + 0x78);
        result = KeBugCheckEx(Arg1, a2, (uint32_t)(Arg1), a4);
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056E784&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0056E784[BB_0056E784]
  bb_0056E79F[BB_0056E79F]
  bb_0056E7B9[BB_0056E7B9]
  bb_0056E7BE[BB_0056E7BE]
  bb_0056E784 -->|branch| bb_0056E7B9
  bb_0056E784 -->|fallthrough| bb_0056E79F
  bb_0056E79F -->|flow| bb_0056E7B9
```
