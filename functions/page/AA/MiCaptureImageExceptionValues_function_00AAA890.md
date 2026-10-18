# MiCaptureImageExceptionValues

- RVA: `0x00AAA890`–`0x00AAA955` (길이 `197` bytes)
- VA: `0x0000000140AAA890`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `51`개 명령, `197/197` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AAA8B3` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x00AAA8BE` → [MiGetExtendedLoaderBitmap](../../text/4F/MiGetExtendedLoaderBitmap_function_004FCC74.md) (function, `0x004FCC74`)
- `0x00AAA8D9` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (function, `0x00450230`)
- `0x00AAA90F` → [RtlMarkExceptionHandlingPages](../A2/RtlMarkExceptionHandlingPages_function_00A26D60.md) (function, `0x00A26D60`)
- `0x00AAA92C` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x00AAA934` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (function, `0x00362490`)

### Direct callers
- [MiConstructLoaderEntry](MiConstructLoaderEntry_function_00AAA264.md) at `0x00AAA6C0`

### Static image references
- `0x00AAA922` → RVA `0x00B09E80` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00AAA8B3` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`PAGE` → `.text`)
  - `0x00AAA8BE` → [MiGetExtendedLoaderBitmap](../../text/4F/MiGetExtendedLoaderBitmap_function_004FCC74.md) (`PAGE` → `.text`)
  - `0x00AAA8D9` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (`PAGE` → `.text`)
  - `0x00AAA92C` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (`PAGE` → `.text`)
  - `0x00AAA934` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAA890  48 8B C4                        mov rax, rsp
00AAA893  48 89 58 08                     mov qword ptr [rax + 8], rbx
00AAA897  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00AAA89B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00AAA89F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00AAA8A3  41 56                           push r14
00AAA8A5  48 83 EC 30                     sub rsp, 0x30
00AAA8A9  48 8B 69 30                     mov rbp, qword ptr [rcx + 0x30]
00AAA8AD  48 8B D9                        mov rbx, rcx
00AAA8B0  48 8B CD                        mov rcx, rbp
00AAA8B3  E8 A8 92 99 FF                  call 0x140443b60
00AAA8B8  48 8B CB                        mov rcx, rbx
00AAA8BB  4C 8B F0                        mov r14, rax
00AAA8BE  E8 B1 23 A5 FF                  call 0x1404fcc74
00AAA8C3  8B 73 40                        mov esi, dword ptr [rbx + 0x40]
00AAA8C6  48 8B C8                        mov rcx, rax
00AAA8C9  C1 EE 0C                        shr esi, 0xc
00AAA8CC  48 8B F8                        mov rdi, rax
00AAA8CF  48 8D 50 10                     lea rdx, [rax + 0x10]
00AAA8D3  89 30                           mov dword ptr [rax], esi
00AAA8D5  48 89 50 08                     mov qword ptr [rax + 8], rdx
00AAA8D9  E8 52 59 9A FF                  call 0x140450230
00AAA8DE  41 83 BE 84 00 00 00 03         cmp dword ptr [r14 + 0x84], 3
00AAA8E6  76 51                           jbe 0x140aaa939
00AAA8E8  45 8B 86 A0 00 00 00            mov r8d, dword ptr [r14 + 0xa0]
00AAA8EF  48 8B CD                        mov rcx, rbp
00AAA8F2  8B 93 98 00 00 00               mov edx, dword ptr [rbx + 0x98]
00AAA8F8  4C 03 C5                        add r8, rbp
00AAA8FB  4C 89 43 10                     mov qword ptr [rbx + 0x10], r8
00AAA8FF  45 8B 8E A4 00 00 00            mov r9d, dword ptr [r14 + 0xa4]
00AAA906  44 89 4B 18                     mov dword ptr [rbx + 0x18], r9d
00AAA90A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00AAA90F  E8 4C C4 F7 FF                  call 0x140a26d60
00AAA914  85 C0                           test eax, eax
00AAA916  79 21                           jns 0x140aaa939
00AAA918  33 D2                           xor edx, edx
00AAA91A  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00AAA91E  4C 8D 4B 58                     lea r9, [rbx + 0x58]
00AAA922  4C 8D 05 57 F5 05 00            lea r8, [rip + 0x5f557]
00AAA929  8D 4A 66                        lea ecx, [rdx + 0x66]
00AAA92C  E8 5F E9 8A FF                  call 0x140359290
00AAA931  48 8B CF                        mov rcx, rdi
00AAA934  E8 57 7B 8B FF                  call 0x140362490
00AAA939  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AAA93E  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00AAA943  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AAA948  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00AAA94D  48 83 C4 30                     add rsp, 0x30
00AAA951  41 5E                           pop r14
00AAA953  C3                              ret
00AAA954  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCaptureImageExceptionValues(__int64 a1)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    result = RtlImageNtHeader(*(unsigned __int64 *)(a1 + 48), a2, a3, a4);
    result = MiGetExtendedLoaderBitmap(a1, a2, a3, a4);
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 64))) >> (12));
    *(unsigned int *)(result) = (unsigned int)(v_rsi);
    *(unsigned __int64 *)(result + 8) = result + 16;
    result = RtlClearAllBits(result, result + 16, a3, a4);
    if ((*(unsigned int *)(result + 132)) <= 3) goto loc_00AAA939;
    a3 = ((unsigned int)(*(unsigned int *)(result + 160))) + (*(unsigned __int64 *)(a1 + 48));
    *(unsigned __int64 *)(a1 + 16) = a3;
    *(unsigned int *)(a1 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 164)));
    v_stack_m18 = result;
    result = RtlMarkExceptionHandlingPages(*(unsigned __int64 *)(a1 + 48), (unsigned int)(*(unsigned int *)(a1 + 152)), a3, (unsigned int)(*(unsigned int *)(result + 164)));
    if (sign_flag) {
        a2 = 0;
        v_stack_m18 = (unsigned int)(v_rsi);
        a4 = a1 + 88;
        a3 = v_rip + 390487;
        a1 = a2 + 102;
        result = DbgPrintEx(a1, a2, a3, a4);
        a1 = result;
        result = RtlSetAllBits(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiCaptureImageExceptionValues(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    result = RtlImageNtHeader(*(uint64_t *)(arg1 + 0x30), a2, a3, a4);
    result = MiGetExtendedLoaderBitmap(Arg1, a2, a3, a4);
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x40))) >> (12));
    *(uint32_t *)(result) = (uint32_t)(local_rsi);
    *(uint64_t *)(result + 0x8) = result + 16;
    result = RtlClearAllBits(result, result + 16, a3, a4);
    if ((*(uint32_t *)(result + 0x84)) <= 3) goto loc_00AAA939;
    a3 = ((uint32_t)(*(uint32_t *)(result + 0xA0))) + (*(uint64_t *)(arg1 + 0x30));
    *(uint64_t *)(arg1 + 0x10) = a3;
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xA4)));
    v_stack_m18 = result;
    result = RtlMarkExceptionHandlingPages(*(uint64_t *)(arg1 + 0x30), (uint32_t)(*(uint32_t *)(arg1 + 0x98)), a3, (uint32_t)(*(uint32_t *)(result + 0xA4)));
    if (sign_flag) {
        a2 = 0;
        v_stack_m18 = (uint32_t)(local_rsi);
        a4 = Arg1 + 88;
        a3 = v_rip + 390487;
        Arg1 = a2 + 102;
        result = DbgPrintEx(Arg1, a2, a3, a4);
        Arg1 = result;
        result = RtlSetAllBits(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `32` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x98` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAA890&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AAA890[BB_00AAA890]
  bb_00AAA8E8[BB_00AAA8E8]
  bb_00AAA918[BB_00AAA918]
  bb_00AAA939[BB_00AAA939]
  bb_00AAA954[BB_00AAA954]
  bb_00AAA890 -->|branch| bb_00AAA939
  bb_00AAA890 -->|fallthrough| bb_00AAA8E8
  bb_00AAA8E8 -->|branch| bb_00AAA939
  bb_00AAA8E8 -->|fallthrough| bb_00AAA918
  bb_00AAA918 -->|flow| bb_00AAA939
```
