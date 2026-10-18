# HalAllocateCommonBufferVector

- RVA: `0x00550160`–`0x00550234` (길이 `212` bytes)
- VA: `0x0000000140550160`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3AF8`
- 디코드: `55`개 명령, `212/212` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005501C7` → [HalpAllocateCommonBufferVectorInternal](../3E/HalpAllocateCommonBufferVectorInternal_function_003E848C.md) (function, `0x003E848C`)
- `0x00550210` → [HalpAllocateCommonBufferVectorInternal](../3E/HalpAllocateCommonBufferVectorInternal_function_003E848C.md) (function, `0x003E848C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00550160  48 8B C4                        mov rax, rsp
00550163  48 89 58 08                     mov qword ptr [rax + 8], rbx
00550167  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0055016B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0055016F  57                              push rdi
00550170  41 54                           push r12
00550172  41 55                           push r13
00550174  41 56                           push r14
00550176  41 57                           push r15
00550178  48 83 EC 50                     sub rsp, 0x50
0055017C  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
00550184  41 8B E9                        mov ebp, r9d
00550187  4C 8B BC 24 B8 00 00 00         mov r15, qword ptr [rsp + 0xb8]
0055018F  49 8B D8                        mov rbx, r8
00550192  44 8B A4 24 B0 00 00 00         mov r12d, dword ptr [rsp + 0xb0]
0055019A  48 8B FA                        mov rdi, rdx
0055019D  44 8B AC 24 A8 00 00 00         mov r13d, dword ptr [rsp + 0xa8]
005501A5  48 8B F1                        mov rsi, rcx
005501A8  4C 89 70 D0                     mov qword ptr [rax - 0x30], r14
005501AC  C6 40 C8 01                     mov byte ptr [rax - 0x38], 1
005501B0  4C 89 78 C0                     mov qword ptr [rax - 0x40], r15
005501B4  44 89 60 B8                     mov dword ptr [rax - 0x48], r12d
005501B8  44 89 68 B0                     mov dword ptr [rax - 0x50], r13d
005501BC  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
005501C3  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
005501C7  E8 C0 82 E9 FF                  call 0x1403e848c
005501CC  3D 9A 00 00 C0                  cmp eax, 0xc000009a
005501D1  75 42                           jne 0x140550215
005501D3  48 8B 8E 00 02 00 00            mov rcx, qword ptr [rsi + 0x200]
005501DA  83 79 30 02                     cmp dword ptr [rcx + 0x30], 2
005501DE  75 35                           jne 0x140550215
005501E0  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
005501E7  44 8B CD                        mov r9d, ebp
005501EA  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
005501EF  4C 8B C3                        mov r8, rbx
005501F2  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
005501F7  48 8B D7                        mov rdx, rdi
005501FA  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
005501FF  48 8B CE                        mov rcx, rsi
00550202  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00550207  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
0055020C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00550210  E8 77 82 E9 FF                  call 0x1403e848c
00550215  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0055021A  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0055021E  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
00550222  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00550226  49 8B E3                        mov rsp, r11
00550229  41 5F                           pop r15
0055022B  41 5E                           pop r14
0055022D  41 5D                           pop r13
0055022F  41 5C                           pop r12
00550231  5F                              pop rdi
00550232  C3                              ret
00550233  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalAllocateCommonBufferVector(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, unsigned int a6, unsigned int a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int8 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (80);
    *(unsigned __int64 *)(v_rsp - 48) = a9;
    *(unsigned __int8 *)(v_rsp - 56) = 1;
    *(unsigned __int64 *)(v_rsp - 64) = a8;
    *(unsigned int *)(v_rsp - 72) = (unsigned int)((unsigned int)(a7));
    *(unsigned int *)(v_rsp - 80) = (unsigned int)((unsigned int)(a6));
    v_stack_m58 = (unsigned int)((unsigned int)(a5));
    result = HalpAllocateCommonBufferVectorInternal(a1, a2, a3, a4);
    if (((unsigned int)(result)) != 0xC000009AULL) goto loc_00550215;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 512) + 48)) == 2) {
        result = a5;
        a4 = (unsigned int)((unsigned int)(a4));
        v_stack_m30 = a9;
        a3 = a3;
        v_stack_m38 = 0;
        a2 = a2;
        v_stack_m40 = a8;
        a1 = a1;
        v_stack_m48 = (unsigned int)((unsigned int)(a7));
        v_stack_m50 = (unsigned int)((unsigned int)(a6));
        v_stack_m58 = (unsigned int)(result);
        result = HalpAllocateCommonBufferVectorInternal(a1, a2, a3, a4);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalAllocateCommonBufferVector(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, uint32_t Arg6, uint32_t Arg7, int64_t Arg8, int64_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint8_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (80);
    *(uint64_t *)(local_rsp - 0x30) = Arg9;
    *(uint8_t *)(local_rsp - 0x38) = 1;
    *(uint64_t *)(local_rsp - 0x40) = Arg8;
    *(uint32_t *)(local_rsp - 0x48) = (uint32_t)((uint32_t)(Arg7));
    *(uint32_t *)(local_rsp - 0x50) = (uint32_t)((uint32_t)(Arg6));
    v_stack_m58 = (uint32_t)((uint32_t)(Arg5));
    result = HalpAllocateCommonBufferVectorInternal(Arg1, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) != 0xC000009AULL) goto loc_00550215;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x200) + 0x30)) == 2) {
        result = Arg5;
        Arg4 = (uint32_t)((uint32_t)(Arg4));
        v_stack_m30 = Arg9;
        Arg3 = Arg3;
        v_stack_m38 = 0;
        Arg2 = Arg2;
        v_stack_m40 = Arg8;
        Arg1 = Arg1;
        v_stack_m48 = (uint32_t)((uint32_t)(Arg7));
        v_stack_m50 = (uint32_t)((uint32_t)(Arg6));
        v_stack_m58 = (uint32_t)(result);
        result = HalpAllocateCommonBufferVectorInternal(Arg1, Arg2, Arg3, Arg4);
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x200` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00550160&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00550160[BB_00550160]
  bb_005501D3[BB_005501D3]
  bb_005501E0[BB_005501E0]
  bb_00550215[BB_00550215]
  bb_00550233[BB_00550233]
  bb_00550160 -->|branch| bb_00550215
  bb_00550160 -->|fallthrough| bb_005501D3
  bb_005501D3 -->|branch| bb_00550215
  bb_005501D3 -->|fallthrough| bb_005501E0
  bb_005501E0 -->|flow| bb_00550215
```
