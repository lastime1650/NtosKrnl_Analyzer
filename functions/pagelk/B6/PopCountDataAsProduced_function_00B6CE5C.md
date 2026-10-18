# PopCountDataAsProduced

- RVA: `0x00B6CE5C`–`0x00B6CF54` (길이 `248` bytes)
- VA: `0x0000000140B6CE5C`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075C18`
- 디코드: `75`개 명령, `248/248` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B6CEB3` → [ProducerGetBuffer](../B7/ProducerGetBuffer_function_00B706C8.md) (function, `0x00B706C8`)
- `0x00B6CECE` → [ProducerConsumerCopyToContextBuffer](../B7/ProducerConsumerCopyToContextBuffer_function_00B7063C.md) (function, `0x00B7063C`)
- `0x00B6CEDF` → [ProducerConsumerCopyToContextBuffer](../B7/ProducerConsumerCopyToContextBuffer_function_00B7063C.md) (function, `0x00B7063C`)
- `0x00B6CF00` → [ProducerConsumerCopyToContextBuffer](../B7/ProducerConsumerCopyToContextBuffer_function_00B7063C.md) (function, `0x00B7063C`)
- `0x00B6CF1F` → [ProducerConsumerBufferComplete](../B7/ProducerConsumerBufferComplete_function_00B704E4.md) (function, `0x00B704E4`)

### Direct callers
- [PopCompressHiberBlocks](PopCompressHiberBlocks_function_00B6CD74.md) at `0x00B6CE2A`
- [PopWriteHiberImage](PopWriteHiberImage_function_00B6FE30.md) at `0x00B6FF2B`

### Static image references
- `0x00B6CE7E` → RVA `0x00F0BFC8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B6CE5C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B6CE61  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00B6CE66  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00B6CE6B  57                              push rdi
00B6CE6C  41 54                           push r12
00B6CE6E  41 55                           push r13
00B6CE70  41 56                           push r14
00B6CE72  41 57                           push r15
00B6CE74  48 83 EC 20                     sub rsp, 0x20
00B6CE78  41 8B 00                        mov eax, dword ptr [r8]
00B6CE7B  4D 8B F0                        mov r14, r8
00B6CE7E  48 8B 3D 43 F1 39 00            mov rdi, qword ptr [rip + 0x39f143]
00B6CE85  4D 8B E1                        mov r12, r9
00B6CE88  44 8B 44 24 70                  mov r8d, dword ptr [rsp + 0x70]
00B6CE8D  4C 8B EA                        mov r13, rdx
00B6CE90  44 8B 4C 24 78                  mov r9d, dword ptr [rsp + 0x78]
00B6CE95  4C 8B F9                        mov r15, rcx
00B6CE98  0F B6 D8                        movzx ebx, al
00B6CE9B  48 8B CF                        mov rcx, rdi
00B6CE9E  C1 E8 08                        shr eax, 8
00B6CEA1  25 FF FF 1F 00                  and eax, 0x1fffff
00B6CEA6  C1 E3 03                        shl ebx, 3
00B6CEA9  41 C1 E0 0C                     shl r8d, 0xc
00B6CEAD  8D 2C 18                        lea ebp, [rax + rbx]
00B6CEB0  8D 55 04                        lea edx, [rbp + 4]
00B6CEB3  E8 10 38 00 00                  call 0x140b706c8
00B6CEB8  48 8B F0                        mov rsi, rax
00B6CEBB  33 C0                           xor eax, eax
00B6CEBD  48 85 F6                        test rsi, rsi
00B6CEC0  74 74                           je 0x140b6cf36
00B6CEC2  4C 8B CE                        mov r9, rsi
00B6CEC5  8D 50 04                        lea edx, [rax + 4]
00B6CEC8  4C 8B C7                        mov r8, rdi
00B6CECB  49 8B CE                        mov rcx, r14
00B6CECE  E8 69 37 00 00                  call 0x140b7063c
00B6CED3  4C 8D 4E 04                     lea r9, [rsi + 4]
00B6CED7  4C 8B C7                        mov r8, rdi
00B6CEDA  8B D3                           mov edx, ebx
00B6CEDC  49 8B CC                        mov rcx, r12
00B6CEDF  E8 58 37 00 00                  call 0x140b7063c
00B6CEE4  41 8B 16                        mov edx, dword ptr [r14]
00B6CEE7  4C 8B C7                        mov r8, rdi
00B6CEEA  C1 EA 08                        shr edx, 8
00B6CEED  49 8B CD                        mov rcx, r13
00B6CEF0  44 8B CB                        mov r9d, ebx
00B6CEF3  81 E2 FF FF 1F 00               and edx, 0x1fffff
00B6CEF9  49 83 C1 04                     add r9, 4
00B6CEFD  4C 03 CE                        add r9, rsi
00B6CF00  E8 37 37 00 00                  call 0x140b7063c
00B6CF05  0F 31                           rdtsc
00B6CF07  48 C1 E2 20                     shl rdx, 0x20
00B6CF0B  44 8D 4D 04                     lea r9d, [rbp + 4]
00B6CF0F  48 0B C2                        or rax, rdx
00B6CF12  4C 8B C6                        mov r8, rsi
00B6CF15  48 8D 57 20                     lea rdx, [rdi + 0x20]
00B6CF19  48 8B CF                        mov rcx, rdi
00B6CF1C  48 8B D8                        mov rbx, rax
00B6CF1F  E8 C0 35 00 00                  call 0x140b704e4
00B6CF24  0F 31                           rdtsc
00B6CF26  48 C1 E2 20                     shl rdx, 0x20
00B6CF2A  48 0B C2                        or rax, rdx
00B6CF2D  48 2B C3                        sub rax, rbx
00B6CF30  49 01 47 50                     add qword ptr [r15 + 0x50], rax
00B6CF34  B0 01                           mov al, 1
00B6CF36  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00B6CF3B  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00B6CF40  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00B6CF45  48 83 C4 20                     add rsp, 0x20
00B6CF49  41 5F                           pop r15
00B6CF4B  41 5E                           pop r14
00B6CF4D  41 5D                           pop r13
00B6CF4F  41 5C                           pop r12
00B6CF51  5F                              pop rdi
00B6CF52  C3                              ret
00B6CF53  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopCountDataAsProduced(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) >> (8));
    result = (unsigned int)((result) & (0x1FFFFFULL));
    v_rbx = (unsigned int)(((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) << (3));
    a3 = (unsigned int)(((unsigned int)(a5)) << (12));
    result = ProducerGetBuffer(*(unsigned __int64 *)(v_rip + 3797315), result + v_rbx * 1 + 4, a3, (unsigned int)(a6));
    result = 0;
    if (0 != 0) {
        a4 = 0;
        a2 = result + 4;
        a3 = *(unsigned __int64 *)(v_rip + 3797315);
        a1 = a3;
        result = ProducerConsumerCopyToContextBuffer(a1, a2, a3, a4);
        a4 = result + 4;
        a3 = *(unsigned __int64 *)(v_rip + 3797315);
        a2 = (unsigned int)(v_rbx);
        a1 = a4;
        result = ProducerConsumerCopyToContextBuffer(a1, a2, a3, a4);
        a2 = *(unsigned int *)(a3);
        a3 = *(unsigned __int64 *)(v_rip + 3797315);
        a2 = (unsigned int)((a2) >> (8));
        a1 = a2;
        a4 = (unsigned int)(v_rbx);
        a2 = (unsigned int)((a2) & (0x1FFFFFULL));
        a4 = (a4) + (4);
        a4 = (a4) + (result);
        result = ProducerConsumerCopyToContextBuffer(a1, a2, a3, a4);
        a2 = (a2) << (32);
        a4 = result + v_rbx * 1 + 4;
        result = (result) | (a2);
        a3 = result;
        a2 = *(unsigned __int64 *)(v_rip + 3797315) + 32;
        a1 = *(unsigned __int64 *)(v_rip + 3797315);
        v_rbx = result;
        result = ProducerConsumerBufferComplete(a1, a2, a3, a4);
        a2 = (a2) << (32);
        result = (result) | (a2);
        result = (result) - (v_rbx);
        result = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopCountDataAsProduced(void *Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3))) >> (8));
    result = (uint32_t)((result) & (0x1FFFFFULL));
    local_rbx = (uint32_t)(((uint8_t)((uint32_t)(*(uint32_t *)(arg3)))) << (3));
    Arg3 = (uint32_t)(((uint32_t)(Arg5)) << (12));
    result = ProducerGetBuffer(*(uint64_t *)(v_rip + 0x39F143), result + local_rbx * 1 + 4, Arg3, (uint32_t)(Arg6));
    result = 0;
    if (0 != 0) {
        Arg4 = 0;
        Arg2 = result + 4;
        Arg3 = *(uint64_t *)(v_rip + 0x39F143);
        Arg1 = Arg3;
        result = ProducerConsumerCopyToContextBuffer(Arg1, Arg2, Arg3, Arg4);
        Arg4 = result + 4;
        Arg3 = *(uint64_t *)(v_rip + 0x39F143);
        Arg2 = (uint32_t)(local_rbx);
        Arg1 = Arg4;
        result = ProducerConsumerCopyToContextBuffer(Arg1, Arg2, Arg3, Arg4);
        Arg2 = *(uint32_t *)(arg3);
        Arg3 = *(uint64_t *)(v_rip + 0x39F143);
        Arg2 = (uint32_t)((Arg2) >> (8));
        Arg1 = Arg2;
        Arg4 = (uint32_t)(local_rbx);
        Arg2 = (uint32_t)((Arg2) & (0x1FFFFFULL));
        Arg4 = (Arg4) + (4);
        Arg4 = (Arg4) + (result);
        result = ProducerConsumerCopyToContextBuffer(Arg1, Arg2, Arg3, Arg4);
        Arg2 = (Arg2) << (32);
        Arg4 = result + local_rbx * 1 + 4;
        result = (result) | (Arg2);
        Arg3 = result;
        Arg2 = *(uint64_t *)(v_rip + 0x39F143) + 32;
        Arg1 = *(uint64_t *)(v_rip + 0x39F143);
        local_rbx = result;
        result = ProducerConsumerBufferComplete(Arg1, Arg2, Arg3, Arg4);
        Arg2 = (Arg2) << (32);
        result = (result) | (Arg2);
        result = (result) - (local_rbx);
        result = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x50` | `64` | `R/W` |
| `Arg3` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B6CE5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B6CE5C[BB_00B6CE5C]
  bb_00B6CEC2[BB_00B6CEC2]
  bb_00B6CF36[BB_00B6CF36]
  bb_00B6CF53[BB_00B6CF53]
  bb_00B6CE5C -->|branch| bb_00B6CF36
  bb_00B6CE5C -->|fallthrough| bb_00B6CEC2
  bb_00B6CEC2 -->|flow| bb_00B6CF36
```
