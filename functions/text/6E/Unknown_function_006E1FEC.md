# sub_006E1FEC

- RVA: `0x006E1FEC`–`0x006E201A` (길이 `46` bytes)
- VA: `0x00000001406E1FEC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076C74`
- 디코드: `11`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E2009` → [MiDeleteKernelStackPages](../2D/MiDeleteKernelStackPages_function_002D9938.md) (function, `0x002D9938`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E2015` → [MmDeleteKernelStack + 0x426](../33/MmDeleteKernelStack_function_0033A960.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E1FEC  41 0F B6 C4                     movzx eax, r12b
006E1FF0  44 0F 22 C0                     mov cr8, rax
006E1FF4  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
006E1FF8  45 8B CE                        mov r9d, r14d
006E1FFB  4D 8B C5                        mov r8, r13
006E1FFE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006E2003  48 8B D5                        mov rdx, rbp
006E2006  48 8B CF                        mov rcx, rdi
006E2009  E8 2A 79 BF FF                  call 0x1402d9938
006E200E  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
006E2015  E9 6C 8D C5 FF                  jmp 0x14033ad86
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E1FEC(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, unsigned int a26)
{
    __int64 result;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = *(unsigned __int64 *)(v_rbx + 40);
    result = MiDeleteKernelStackPages(v_rdi, v_rbp, v_r13, (unsigned int)((unsigned int)(v_r14)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E1FEC(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint32_t Arg26)
{
    int64_t result;
    uint64_t v_stack_p20;

    v_stack_p20 = *(uint64_t *)(local_rbx + 0x28);
    result = MiDeleteKernelStackPages(local_rdi, local_rbp, local_r13, (uint32_t)((uint32_t)(local_r14)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E1FEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E1FEC[BB_006E1FEC]
```
