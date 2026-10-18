# HalpMmAllocatePerProcessorMemory

- RVA: `0x00544AA8`–`0x00544AEC` (길이 `68` bytes)
- VA: `0x0000000140544AA8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `22`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00544AB4` → [HalQueryMaximumProcessorCount](../4A/HalQueryMaximumProcessorCount_function_004AC9A0.md) (function, `0x004AC9A0`)
- `0x00544AC3` → [HalpMmAllocateMemoryInternal](HalpMmAllocateMemoryInternal_function_00544990.md) (function, `0x00544990`)
- `0x00544AD8` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [HalpTimerInitializeProfiling](HalpTimerInitializeProfiling_function_0054B4FC.md) at `0x0054B534`
- [HalpInitializePmcCounterSetInfo](../../init/C1/HalpInitializePmcCounterSetInfo_function_00C1EEC4.md) at `0x00C1EEDA`
- [HalpInitializePmcCounterSetInfo](../../init/C1/HalpInitializePmcCounterSetInfo_function_00C1EEC4.md) at `0x00C1EF50`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00544AA8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00544AAD  57                              push rdi
00544AAE  48 83 EC 20                     sub rsp, 0x20
00544AB2  8B F9                           mov edi, ecx
00544AB4  E8 E7 7E F6 FF                  call 0x1404ac9a0
00544AB9  0F AF F8                        imul edi, eax
00544ABC  BA 01 00 00 00                  mov edx, 1
00544AC1  8B CF                           mov ecx, edi
00544AC3  E8 C8 FE FF FF                  call 0x140544990
00544AC8  48 8B D8                        mov rbx, rax
00544ACB  48 85 C0                        test rax, rax
00544ACE  74 0D                           je 0x140544add
00544AD0  44 8B C7                        mov r8d, edi
00544AD3  33 D2                           xor edx, edx
00544AD5  48 8B C8                        mov rcx, rax
00544AD8  E8 63 21 18 00                  call 0x1406c6c40
00544ADD  48 8B C3                        mov rax, rbx
00544AE0  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00544AE5  48 83 C4 20                     add rsp, 0x20
00544AE9  5F                              pop rdi
00544AEA  C3                              ret
00544AEB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpMmAllocatePerProcessorMemory(int a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = HalQueryMaximumProcessorCount(a1, a2, a3, a4);
    v_rdi = (unsigned int)(((unsigned int)(a1)) * ((unsigned int)(result)));
    result = HalpMmAllocateMemoryInternal((unsigned int)((unsigned int)(v_rdi)), 1, a3, a4);
    if (result != 0) {
        a3 = (unsigned int)(v_rdi);
        a2 = 0;
        a1 = result;
        result = memset(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpMmAllocatePerProcessorMemory(int32_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = HalQueryMaximumProcessorCount(Arg1, a2, a3, a4);
    local_rdi = (uint32_t)(((uint32_t)(Arg1)) * ((uint32_t)(result)));
    result = HalpMmAllocateMemoryInternal((uint32_t)((uint32_t)(local_rdi)), 1, a3, a4);
    if (result != 0) {
        a3 = (uint32_t)(local_rdi);
        a2 = 0;
        Arg1 = result;
        result = memset(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00544AA8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00544AA8[BB_00544AA8]
  bb_00544AD0[BB_00544AD0]
  bb_00544ADD[BB_00544ADD]
  bb_00544AEB[BB_00544AEB]
  bb_00544AA8 -->|branch| bb_00544ADD
  bb_00544AA8 -->|fallthrough| bb_00544AD0
  bb_00544AD0 -->|flow| bb_00544ADD
```
