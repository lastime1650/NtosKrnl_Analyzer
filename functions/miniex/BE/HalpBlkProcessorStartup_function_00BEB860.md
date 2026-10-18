# HalpBlkProcessorStartup

- RVA: `0x00BEB860`–`0x00BEB89E` (길이 `62` bytes)
- VA: `0x0000000140BEB860`
- 실행 섹션: `MINIEX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFB20`
- 디코드: `16`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BEB884` → [HalpBlkApicInitializeLocalUnit](HalpBlkApicInitializeLocalUnit_function_00BEB1F0.md) (function, `0x00BEB1F0`)
- `0x00BEB889` → [HalpBlkMceInitialize](HalpBlkMceInitialize_function_00BEB790.md) (function, `0x00BEB790`)
- `0x00BEB898` → [HalpBlkIdleLoop](HalpBlkIdleLoop_function_00BEB7D0.md) (function, `0x00BEB7D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BEB860  48 83 EC 38                     sub rsp, 0x38
00BEB864  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00BEB869  4C 8B FC                        mov r15, rsp
00BEB86C  FA                              cli
00BEB86D  48 8B D1                        mov rdx, rcx
00BEB870  8B C2                           mov eax, edx
00BEB872  48 C1 EA 20                     shr rdx, 0x20
00BEB876  B9 01 01 00 C0                  mov ecx, 0xc0000101
00BEB87B  0F 30                           wrmsr
00BEB87D  B9 02 01 00 C0                  mov ecx, 0xc0000102
00BEB882  0F 30                           wrmsr
00BEB884  E8 67 F9 FF FF                  call 0x140beb1f0
00BEB889  E8 02 FF FF FF                  call 0x140beb790
00BEB88E  65 F0 48 FF 04 25 10 00 00 00   lock inc qword ptr gs:[0x10]
00BEB898  E8 33 FF FF FF                  call 0x140beb7d0
00BEB89D  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpBlkProcessorStartup(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m8;

    v_rsp = (v_rsp) - (56);
    v_stack_m8 = v_r15;
    a2 = (a1) >> (32);
    result = HalpBlkApicInitializeLocalUnit((unsigned int)(0xC0000102ULL), a2, a3, a4);
    result = HalpBlkMceInitialize((unsigned int)(0xC0000102ULL), a2, a3, a4);
    result = HalpBlkIdleLoop((unsigned int)(0xC0000102ULL), a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpBlkProcessorStartup(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m8;

    local_rsp = (local_rsp) - (56);
    v_stack_m8 = local_r15;
    a2 = (Arg1) >> (32);
    result = HalpBlkApicInitializeLocalUnit((uint32_t)(0xC0000102ULL), a2, a3, a4);
    result = HalpBlkMceInitialize((uint32_t)(0xC0000102ULL), a2, a3, a4);
    result = HalpBlkIdleLoop((uint32_t)(0xC0000102ULL), a2, a3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=miniex&rva=0x00BEB860&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BEB860[BB_00BEB860]
```
