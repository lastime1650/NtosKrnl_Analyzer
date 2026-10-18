# SymCryptFdefModAddMulx256Asm

- RVA: `0x005301F0`–`0x00530280` (길이 `144` bytes)
- VA: `0x00000001405301F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3520`
- 디코드: `35`개 명령, `144/144` bytes 표시
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
005301F0  48 56                           push rsi
005301F2  57                              push rdi
005301F3  48 81 C1 00 01 00 00            add rcx, 0x100
005301FA  48 33 C0                        xor rax, rax
005301FD  48 8B 02                        mov rax, qword ptr [rdx]
00530200  66 49 0F 38 F6 00               adcx rax, qword ptr [r8]
00530206  4C 8B 52 08                     mov r10, qword ptr [rdx + 8]
0053020A  66 4D 0F 38 F6 50 08            adcx r10, qword ptr [r8 + 8]
00530211  4C 8B 5A 10                     mov r11, qword ptr [rdx + 0x10]
00530215  66 4D 0F 38 F6 58 10            adcx r11, qword ptr [r8 + 0x10]
0053021C  48 8B 52 18                     mov rdx, qword ptr [rdx + 0x18]
00530220  66 49 0F 38 F6 50 18            adcx rdx, qword ptr [r8 + 0x18]
00530227  48 8B 31                        mov rsi, qword ptr [rcx]
0053022A  F3 48 0F 38 F6 F0               adox rsi, rax
00530230  48 8B 79 08                     mov rdi, qword ptr [rcx + 8]
00530234  F3 49 0F 38 F6 FA               adox rdi, r10
0053023A  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
0053023E  F3 4D 0F 38 F6 C3               adox r8, r11
00530244  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00530248  F3 48 0F 38 F6 CA               adox rcx, rdx
0053024E  48 0F 42 C6                     cmovb rax, rsi
00530252  4C 0F 42 D7                     cmovb r10, rdi
00530256  4D 0F 42 D8                     cmovb r11, r8
0053025A  48 0F 42 D1                     cmovb rdx, rcx
0053025E  48 0F 40 C6                     cmovo rax, rsi
00530262  4C 0F 40 D7                     cmovo r10, rdi
00530266  4D 0F 40 D8                     cmovo r11, r8
0053026A  48 0F 40 D1                     cmovo rdx, rcx
0053026E  49 89 01                        mov qword ptr [r9], rax
00530271  4D 89 51 08                     mov qword ptr [r9 + 8], r10
00530275  4D 89 59 10                     mov qword ptr [r9 + 0x10], r11
00530279  49 89 51 18                     mov qword ptr [r9 + 0x18], rdx
0053027D  5F                              pop rdi
0053027E  5E                              pop rsi
0053027F  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefModAddMulx256Asm(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;

    a1 = (a1) + (256);
    result = 0;
    result = *(unsigned __int64 *)(a2);
    if (condition_is_below) { result = *(unsigned __int64 *)(a1); }
    v_r10 = *(unsigned __int64 *)(a2 + 8);
    if (condition_is_below) { v_r10 = *(unsigned __int64 *)(a1 + 8); }
    v_r11 = *(unsigned __int64 *)(a2 + 16);
    if (condition_is_below) { v_r11 = *(unsigned __int64 *)(a1 + 16); }
    a2 = *(unsigned __int64 *)(a2 + 24);
    if (condition_is_below) { a2 = *(unsigned __int64 *)(a1 + 24); }
    if (overflow_flag) {
        result = *(unsigned __int64 *)(a1);
        v_r10 = *(unsigned __int64 *)(a1 + 8);
        v_r11 = *(unsigned __int64 *)(a1 + 16);
        a2 = *(unsigned __int64 *)(a1 + 24);
    }
    *(unsigned __int64 *)(a4) = result;
    *(unsigned __int64 *)(a4 + 8) = v_r10;
    *(unsigned __int64 *)(a4 + 16) = v_r11;
    *(unsigned __int64 *)(a4 + 24) = a2;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefModAddMulx256Asm(void *Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;

    Arg1 = (Arg1) + (256);
    result = 0;
    result = *(uint64_t *)(arg2);
    if (condition_is_below) { result = *(uint64_t *)(arg1); }
    local_r10 = *(uint64_t *)(arg2 + 0x8);
    if (condition_is_below) { local_r10 = *(uint64_t *)(arg1 + 0x8); }
    local_r11 = *(uint64_t *)(arg2 + 0x10);
    if (condition_is_below) { local_r11 = *(uint64_t *)(arg1 + 0x10); }
    Arg2 = *(uint64_t *)(arg2 + 0x18);
    if (condition_is_below) { Arg2 = *(uint64_t *)(arg1 + 0x18); }
    if (overflow_flag) {
        result = *(uint64_t *)(arg1);
        local_r10 = *(uint64_t *)(arg1 + 0x8);
        local_r11 = *(uint64_t *)(arg1 + 0x10);
        Arg2 = *(uint64_t *)(arg1 + 0x18);
    }
    *(uint64_t *)(arg4) = result;
    *(uint64_t *)(arg4 + 0x8) = local_r10;
    *(uint64_t *)(arg4 + 0x10) = local_r11;
    *(void **)(arg4 + 0x18) = Arg2;
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
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x8` | `64` | `W` |
| `Arg4` | `+ 0x10` | `64` | `W` |
| `Arg4` | `+ 0x18` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005301F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005301F0[BB_005301F0]
```
