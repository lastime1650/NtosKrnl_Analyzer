# HvlDeletePrQueue

- RVA: `0x005874B0`–`0x005874FB` (길이 `75` bytes)
- VA: `0x00000001405874B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082420`
- 디코드: `18`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005874E8` → [HvcallFastExtended](../31/HvcallFastExtended_function_003130E0.md) (function, `0x003130E0`)
- `0x005874F0` → [HvlpHvToNtStatus](../30/HvlpHvToNtStatus_function_00307BD8.md) (function, `0x00307BD8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005874B0  48 8B C4                        mov rax, rsp
005874B3  48 83 EC 48                     sub rsp, 0x48
005874B7  83 60 F4 00                     and dword ptr [rax - 0xc], 0
005874BB  48 8D 50 E8                     lea rdx, [rax - 0x18]
005874BF  48 83 48 E8 FF                  or qword ptr [rax - 0x18], 0xffffffffffffffff
005874C4  45 33 C9                        xor r9d, r9d
005874C7  83 60 D8 00                     and dword ptr [rax - 0x28], 0
005874CB  48 C7 44 24 58 A8 00 00 00      mov qword ptr [rsp + 0x58], 0xa8
005874D4  89 48 F0                        mov dword ptr [rax - 0x10], ecx
005874D7  C7 44 24 58 A8 00 01 00         mov dword ptr [rsp + 0x58], 0x100a8
005874DF  45 8D 41 10                     lea r8d, [r9 + 0x10]
005874E3  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
005874E8  E8 F3 BB D8 FF                  call 0x1403130e0
005874ED  48 8B C8                        mov rcx, rax
005874F0  E8 E3 06 D8 FF                  call 0x140307bd8
005874F5  48 83 C4 48                     add rsp, 0x48
005874F9  C3                              ret
005874FA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlDeletePrQueue(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (72);
    a4 = 0;
    v_stack_p10 = 168;
    *(unsigned int *)(v_rsp - 16) = a1;
    v_stack_p10 = 0x100A8ULL;
    result = HvcallFastExtended(v_stack_p10, v_rsp - 24, a4 + 16, a4);
    result = HvlpHvToNtStatus(result, v_rsp - 24, a4 + 16, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlDeletePrQueue(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (72);
    Arg4 = 0;
    v_stack_p10 = 168;
    *(uint32_t *)(local_rsp - 0x10) = Arg1;
    v_stack_p10 = 0x100A8ULL;
    result = HvcallFastExtended(v_stack_p10, local_rsp - 24, Arg4 + 16, Arg4);
    result = HvlpHvToNtStatus(result, local_rsp - 24, Arg4 + 16, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005874B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005874B0[BB_005874B0]
  bb_005874FA[BB_005874FA]
```
