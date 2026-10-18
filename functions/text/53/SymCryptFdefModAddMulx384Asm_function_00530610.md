# SymCryptFdefModAddMulx384Asm

- RVA: `0x00530610`–`0x005306EE` (길이 `222` bytes)
- VA: `0x0000000140530610`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3548`
- 디코드: `57`개 명령, `222/222` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00530610  48 56                           push rsi
00530612  57                              push rdi
00530613  55                              push rbp
00530614  53                              push rbx
00530615  41 54                           push r12
00530617  41 55                           push r13
00530619  48 81 C1 00 01 00 00            add rcx, 0x100
00530620  48 33 C0                        xor rax, rax
00530623  48 8B 02                        mov rax, qword ptr [rdx]
00530626  66 49 0F 38 F6 00               adcx rax, qword ptr [r8]
0053062C  4C 8B 52 08                     mov r10, qword ptr [rdx + 8]
00530630  66 4D 0F 38 F6 50 08            adcx r10, qword ptr [r8 + 8]
00530637  4C 8B 5A 10                     mov r11, qword ptr [rdx + 0x10]
0053063B  66 4D 0F 38 F6 58 10            adcx r11, qword ptr [r8 + 0x10]
00530642  48 8B 72 18                     mov rsi, qword ptr [rdx + 0x18]
00530646  66 49 0F 38 F6 70 18            adcx rsi, qword ptr [r8 + 0x18]
0053064D  48 8B 7A 20                     mov rdi, qword ptr [rdx + 0x20]
00530651  66 49 0F 38 F6 78 20            adcx rdi, qword ptr [r8 + 0x20]
00530658  48 8B 52 28                     mov rdx, qword ptr [rdx + 0x28]
0053065C  66 49 0F 38 F6 50 28            adcx rdx, qword ptr [r8 + 0x28]
00530663  48 8B 29                        mov rbp, qword ptr [rcx]
00530666  F3 48 0F 38 F6 E8               adox rbp, rax
0053066C  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
00530670  F3 49 0F 38 F6 DA               adox rbx, r10
00530676  4C 8B 61 10                     mov r12, qword ptr [rcx + 0x10]
0053067A  F3 4D 0F 38 F6 E3               adox r12, r11
00530680  4C 8B 69 18                     mov r13, qword ptr [rcx + 0x18]
00530684  F3 4C 0F 38 F6 EE               adox r13, rsi
0053068A  4C 8B 41 20                     mov r8, qword ptr [rcx + 0x20]
0053068E  F3 4C 0F 38 F6 C7               adox r8, rdi
00530694  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
00530698  F3 48 0F 38 F6 CA               adox rcx, rdx
0053069E  48 0F 42 C5                     cmovb rax, rbp
005306A2  4C 0F 42 D3                     cmovb r10, rbx
005306A6  4D 0F 42 DC                     cmovb r11, r12
005306AA  49 0F 42 F5                     cmovb rsi, r13
005306AE  49 0F 42 F8                     cmovb rdi, r8
005306B2  48 0F 42 D1                     cmovb rdx, rcx
005306B6  48 0F 40 C5                     cmovo rax, rbp
005306BA  4C 0F 40 D3                     cmovo r10, rbx
005306BE  4D 0F 40 DC                     cmovo r11, r12
005306C2  49 0F 40 F5                     cmovo rsi, r13
005306C6  49 0F 40 F8                     cmovo rdi, r8
005306CA  48 0F 40 D1                     cmovo rdx, rcx
005306CE  49 89 01                        mov qword ptr [r9], rax
005306D1  4D 89 51 08                     mov qword ptr [r9 + 8], r10
005306D5  4D 89 59 10                     mov qword ptr [r9 + 0x10], r11
005306D9  49 89 71 18                     mov qword ptr [r9 + 0x18], rsi
005306DD  49 89 79 20                     mov qword ptr [r9 + 0x20], rdi
005306E1  49 89 51 28                     mov qword ptr [r9 + 0x28], rdx
005306E5  41 5D                           pop r13
005306E7  41 5C                           pop r12
005306E9  5B                              pop rbx
005306EA  5D                              pop rbp
005306EB  5F                              pop rdi
005306EC  5E                              pop rsi
005306ED  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefModAddMulx384Asm(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rdi;
    __int64 v_rsi;

    a1 = (a1) + (256);
    result = 0;
    result = *(unsigned __int64 *)(a2);
    if (condition_is_below) { result = *(unsigned __int64 *)(a1); }
    v_r10 = *(unsigned __int64 *)(a2 + 8);
    if (condition_is_below) { v_r10 = *(unsigned __int64 *)(a1 + 8); }
    v_r11 = *(unsigned __int64 *)(a2 + 16);
    if (condition_is_below) { v_r11 = *(unsigned __int64 *)(a1 + 16); }
    v_rsi = *(unsigned __int64 *)(a2 + 24);
    if (condition_is_below) { v_rsi = *(unsigned __int64 *)(a1 + 24); }
    v_rdi = *(unsigned __int64 *)(a2 + 32);
    if (condition_is_below) { v_rdi = *(unsigned __int64 *)(a1 + 32); }
    a2 = *(unsigned __int64 *)(a2 + 40);
    if (condition_is_below) { a2 = *(unsigned __int64 *)(a1 + 40); }
    if (overflow_flag) {
        result = *(unsigned __int64 *)(a1);
        v_r10 = *(unsigned __int64 *)(a1 + 8);
        v_r11 = *(unsigned __int64 *)(a1 + 16);
        v_rsi = *(unsigned __int64 *)(a1 + 24);
        v_rdi = *(unsigned __int64 *)(a1 + 32);
        a2 = *(unsigned __int64 *)(a1 + 40);
    }
    *(unsigned __int64 *)(a4) = result;
    *(unsigned __int64 *)(a4 + 8) = v_r10;
    *(unsigned __int64 *)(a4 + 16) = v_r11;
    *(unsigned __int64 *)(a4 + 24) = v_rsi;
    *(unsigned __int64 *)(a4 + 32) = v_rdi;
    *(unsigned __int64 *)(a4 + 40) = a2;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefModAddMulx384Asm(void *Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rdi;
    int64_t local_rsi;

    Arg1 = (Arg1) + (256);
    result = 0;
    result = *(uint64_t *)(arg2);
    if (condition_is_below) { result = *(uint64_t *)(arg1); }
    local_r10 = *(uint64_t *)(arg2 + 0x8);
    if (condition_is_below) { local_r10 = *(uint64_t *)(arg1 + 0x8); }
    local_r11 = *(uint64_t *)(arg2 + 0x10);
    if (condition_is_below) { local_r11 = *(uint64_t *)(arg1 + 0x10); }
    local_rsi = *(uint64_t *)(arg2 + 0x18);
    if (condition_is_below) { local_rsi = *(uint64_t *)(arg1 + 0x18); }
    local_rdi = *(uint64_t *)(arg2 + 0x20);
    if (condition_is_below) { local_rdi = *(uint64_t *)(arg1 + 0x20); }
    Arg2 = *(uint64_t *)(arg2 + 0x28);
    if (condition_is_below) { Arg2 = *(uint64_t *)(arg1 + 0x28); }
    if (overflow_flag) {
        result = *(uint64_t *)(arg1);
        local_r10 = *(uint64_t *)(arg1 + 0x8);
        local_r11 = *(uint64_t *)(arg1 + 0x10);
        local_rsi = *(uint64_t *)(arg1 + 0x18);
        local_rdi = *(uint64_t *)(arg1 + 0x20);
        Arg2 = *(uint64_t *)(arg1 + 0x28);
    }
    *(uint64_t *)(arg4) = result;
    *(uint64_t *)(arg4 + 0x8) = local_r10;
    *(uint64_t *)(arg4 + 0x10) = local_r11;
    *(uint64_t *)(arg4 + 0x18) = local_rsi;
    *(uint64_t *)(arg4 + 0x20) = local_rdi;
    *(void **)(arg4 + 0x28) = Arg2;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x28` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x8` | `64` | `W` |
| `Arg4` | `+ 0x10` | `64` | `W` |
| `Arg4` | `+ 0x18` | `64` | `W` |
| `Arg4` | `+ 0x20` | `64` | `W` |
| `Arg4` | `+ 0x28` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00530610&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00530610[BB_00530610]
```
