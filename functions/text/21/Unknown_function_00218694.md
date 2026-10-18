# sub_00218694

- RVA: `0x00218694`–`0x002187BE` (길이 `298` bytes)
- VA: `0x0000000140218694`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005E9D4`
- 디코드: `60`개 명령, `298/298` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00218773` → [KiSetAddressPolicy](KiSetAddressPolicy_function_002178A0.md) (function, `0x002178A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0021873E` → RVA `0x01201840` (`CFGRO`; read)
- `0x00218778` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002187AB` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x0021869D` → [sub_002189F1](Unknown_function_002189F1.md) (`tail-transfer`)
  - `0x002186C6` → [sub_0021889D](Unknown_function_0021889D.md) (`tail-transfer`)
  - `0x002186E6` → [sub_0021889D + 0x17](Unknown_function_0021889D.md) (`tail-transfer`)
  - `0x00218780` → [sub_00218A8C](Unknown_function_00218A8C.md) (`tail-transfer`)
  - `0x00218790` → [sub_0021889D + 0x2E](Unknown_function_0021889D.md) (`tail-transfer`)
  - `0x002187BC` → [sub_002187BE + 0xD](Unknown_function_002187BE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00218694  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00218699  90                              nop
0021869A  48 3B F1                        cmp rsi, rcx
0021869D  0F 85 4E 03 00 00               jne 0x1402189f1
002186A3  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
002186A7  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
002186AB  0F B6 41 28                     movzx eax, byte ptr [rcx + 0x28]
002186AF  88 47 28                        mov byte ptr [rdi + 0x28], al
002186B2  0F B6 41 29                     movzx eax, byte ptr [rcx + 0x29]
002186B6  88 47 29                        mov byte ptr [rdi + 0x29], al
002186B9  0F B6 41 2A                     movzx eax, byte ptr [rcx + 0x2a]
002186BD  88 47 2A                        mov byte ptr [rdi + 0x2a], al
002186C0  48 8B 11                        mov rdx, qword ptr [rcx]
002186C3  48 3B D1                        cmp rdx, rcx
002186C6  0F 85 D1 01 00 00               jne 0x14021889d
002186CC  48 89 7F 08                     mov qword ptr [rdi + 8], rdi
002186D0  48 89 3F                        mov qword ptr [rdi], rdi
002186D3  40 88 6F 29                     mov byte ptr [rdi + 0x29], bpl
002186D7  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
002186DB  48 8D 41 10                     lea rax, [rcx + 0x10]
002186DF  48 3B D0                        cmp rdx, rax
002186E2  48 8D 47 10                     lea rax, [rdi + 0x10]
002186E6  0F 85 C8 01 00 00               jne 0x1402188b4
002186EC  48 89 40 08                     mov qword ptr [rax + 8], rax
002186F0  48 89 00                        mov qword ptr [rax], rax
002186F3  40 88 6F 2A                     mov byte ptr [rdi + 0x2a], bpl
002186F7  48 89 AB 78 02 00 00            mov qword ptr [rbx + 0x278], rbp
002186FE  40 88 AB 4A 02 00 00            mov byte ptr [rbx + 0x24a], bpl
00218705  48 89 6B 40                     mov qword ptr [rbx + 0x40], rbp
00218709  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00218712  4C 8B 83 B8 00 00 00            mov r8, qword ptr [rbx + 0xb8]
00218719  44 0F B6 B0 D1 00 00 00         movzx r14d, byte ptr [rax + 0xd1]
00218721  0F B6 80 D0 00 00 00            movzx eax, byte ptr [rax + 0xd0]
00218728  48 8D 2C C5 00 00 00 00         lea rbp, [rax*8]
00218730  49 8B 80 80 00 00 00            mov rax, qword ptr [r8 + 0x80]
00218737  F0 4C 0F AB 74 28 08            lock bts qword ptr [rax + rbp + 8], r14
0021873E  80 3D FB 90 FE 00 00            cmp byte ptr [rip + 0xfe90fb], 0
00218745  49 8B 70 28                     mov rsi, qword ptr [r8 + 0x28]
00218749  74 2D                           je 0x140218778
0021874B  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
00218755  48 8B C6                        mov rax, rsi
00218758  48 0B C1                        or rax, rcx
0021875B  41 84 F4                        test r12b, sil
0021875E  48 0F 44 C6                     cmove rax, rsi
00218762  65 48 89 04 25 00 B0 00 00      mov qword ptr gs:[0xb000], rax
0021876B  41 0F B6 88 60 01 00 00         movzx ecx, byte ptr [r8 + 0x160]
00218773  E8 28 F1 FF FF                  call 0x1402178a0
00218778  8B 05 3A E3 DA 00               mov eax, dword ptr [rip + 0xdae33a]
0021877E  A8 01                           test al, 1
00218780  0F 85 06 03 00 00               jne 0x140218a8c
00218786  0F 22 DE                        mov cr3, rsi
00218789  80 3D B0 90 FE 00 00            cmp byte ptr [rip + 0xfe90b0], 0
00218790  0F 85 35 01 00 00               jne 0x1402188cb
00218796  49 8B 87 80 00 00 00            mov rax, qword ptr [r15 + 0x80]
0021879D  F0 4C 0F B3 74 28 08            lock btr qword ptr [rax + rbp + 8], r14
002187A4  81 63 74 FF F7 FF FF            and dword ptr [rbx + 0x74], 0xfffff7ff
002187AB  83 3D 6E E5 DA 00 00            cmp dword ptr [rip + 0xdae56e], 0
002187B2  0F B6 74 24 70                  movzx esi, byte ptr [rsp + 0x70]
002187B7  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
002187BC  74 0D                           je 0x1402187cb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00218694(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, unsigned __int8 a14)
{
    __int64 result;
    unsigned __int64 v_stack_p48;

    v_stack_p48 = v_r14;
    *(unsigned __int64 *)(v_rdi + 32) = *(unsigned __int64 *)(a1 + 32);
    *(unsigned __int8 *)(v_rdi + 40) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 40));
    *(unsigned __int8 *)(v_rdi + 41) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 41));
    *(unsigned __int8 *)(v_rdi + 42) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 42));
    *(unsigned __int64 *)(v_rdi + 8) = v_rdi;
    *(unsigned __int64 *)(v_rdi) = v_rdi;
    *(unsigned __int8 *)(v_rdi + 41) = (unsigned __int8)(v_rbp);
    *(unsigned __int64 *)(v_rdi + 16 + 8) = v_rdi + 16;
    *(unsigned __int64 *)(v_rdi + 16) = v_rdi + 16;
    *(unsigned __int8 *)(v_rdi + 42) = (unsigned __int8)(v_rbp);
    *(unsigned __int64 *)(v_rbx + 632) = v_rbp;
    *(unsigned __int8 *)(v_rbx + 586) = (unsigned __int8)(v_rbp);
    *(unsigned __int64 *)(v_rbx + 64) = v_rbp;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 184) + 128);
    if ((*(unsigned __int8 *)(v_rip + 16683259)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 184) + 40);
        result = (result) | (a1);
        if ((((unsigned __int8)(v_r12)) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 184) + 40)))) == 0) { result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 184) + 40); }
        *(unsigned __int64 *)(gs_base + (0 + 45056)) = result;
        a1 = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 184) + 352);
        result = KiSetAddressPolicy(a1, *(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)(v_rbx + 184), a4);
    }
}
```

## 5. (Beta) C Style

```c
int64_t sub_00218694(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, int64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint8_t Arg14)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    uint64_t v_stack_p48;

    v_stack_p48 = local_r14;
    *(uint64_t *)(local_rdi + 0x20) = *(uint64_t *)(arg1 + 0x20);
    *(uint8_t *)(local_rdi + 0x28) = (uint8_t)(*(uint8_t *)(arg1 + 0x28));
    *(uint8_t *)(local_rdi + 0x29) = (uint8_t)(*(uint8_t *)(arg1 + 0x29));
    *(uint8_t *)(local_rdi + 0x2A) = (uint8_t)(*(uint8_t *)(arg1 + 0x2A));
    *(uint64_t *)(local_rdi + 0x8) = local_rdi;
    *(uint64_t *)(local_rdi) = local_rdi;
    *(uint8_t *)(local_rdi + 0x29) = (uint8_t)(local_rbp);
    *(uint64_t *)(local_rdi + 0x10 + 0x8) = local_rdi + 16;
    *(uint64_t *)(local_rdi + 0x10) = local_rdi + 16;
    *(uint8_t *)(local_rdi + 0x2A) = (uint8_t)(local_rbp);
    *(uint64_t *)(local_rbx + 0x278) = local_rbp;
    *(uint8_t *)(local_rbx + 0x24A) = (uint8_t)(local_rbp);
    *(uint64_t *)(local_rbx + 0x40) = local_rbp;
    result = *(uint64_t *)(*(uint64_t *)(local_rbx + 0xB8) + 0x80);
    if ((*(uint8_t *)(v_rip + 0xFE90FB)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rbx + 0xB8) + 0x28);
        result = (result) | (Arg1);
        if ((((uint8_t)(local_r12)) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0xB8) + 0x28)))) == 0) { result = *(uint64_t *)(*(uint64_t *)(local_rbx + 0xB8) + 0x28); }
        *(uint64_t *)(gs_base + (0 + 0xB000)) = result;
        Arg1 = *(uint8_t *)(*(uint64_t *)(local_rbx + 0xB8) + 0x160);
        result = KiSetAddressPolicy(Arg1, *(uint64_t *)(arg1 + 0x10), *(uint64_t *)(local_rbx + 0xB8), Arg4);
    }
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `8` | `R` |
| `Arg1` | `+ 0x29` | `8` | `R` |
| `Arg1` | `+ 0x2A` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00218694&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00218694[BB_00218694]
  bb_002186A3[BB_002186A3]
  bb_002186CC[BB_002186CC]
  bb_002186EC[BB_002186EC]
  bb_0021874B[BB_0021874B]
  bb_00218778[BB_00218778]
  bb_00218786[BB_00218786]
  bb_00218796[BB_00218796]
  bb_00218694 -->|fallthrough| bb_002186A3
  bb_002186A3 -->|fallthrough| bb_002186CC
  bb_002186CC -->|fallthrough| bb_002186EC
  bb_002186EC -->|branch| bb_00218778
  bb_002186EC -->|fallthrough| bb_0021874B
  bb_0021874B -->|flow| bb_00218778
  bb_00218778 -->|fallthrough| bb_00218786
  bb_00218786 -->|fallthrough| bb_00218796
```
