# TtmpCallSetDisplayState

- RVA: `0x0077608C`–`0x00776134` (길이 `168` bytes)
- VA: `0x000000014077608C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE9D0`
- 디코드: `48`개 명령, `168/168` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007760DC` → [TtmpStartCallout](TtmpStartCallout_function_00776AA4.md) (function, `0x00776AA4`)
- `0x007760EE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x007760FC` → [TtmpStopCallout](TtmpStopCallout_function_00776C24.md) (function, `0x00776C24`)
- `0x00776118` → [TtmiLogError](../98/TtmiLogError_function_0098B39C.md) (function, `0x0098B39C`)

### Direct callers
- [TtmpPushTerminalDisplayStateOntoDevice](TtmpPushTerminalDisplayStateOntoDevice_function_00776838.md) at `0x0077687E`

### Static image references
- `0x00776109` → RVA `0x00B03FA0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007760EE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077608C  4C 8B DC                        mov r11, rsp
0077608F  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00776093  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00776097  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0077609B  57                              push rdi
0077609C  48 83 EC 60                     sub rsp, 0x60
007760A0  48 8B 7A 38                     mov rdi, qword ptr [rdx + 0x38]
007760A4  41 8B F0                        mov esi, r8d
007760A7  48 8B DA                        mov rbx, rdx
007760AA  48 8B E9                        mov rbp, rcx
007760AD  48 85 FF                        test rdi, rdi
007760B0  74 6B                           je 0x14077611d
007760B2  33 C0                           xor eax, eax
007760B4  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
007760B9  0F 57 C0                        xorps xmm0, xmm0
007760BC  49 89 7B B8                     mov qword ptr [r11 - 0x48], rdi
007760C0  4C 8B C2                        mov r8, rdx
007760C3  48 8B D1                        mov rdx, rcx
007760C6  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
007760CB  44 8D 48 04                     lea r9d, [rax + 4]
007760CF  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
007760D4  49 8D 4B C8                     lea rcx, [r11 - 0x38]
007760D8  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
007760DC  E8 C3 09 00 00                  call 0x140776aa4
007760E1  44 8B 45 78                     mov r8d, dword ptr [rbp + 0x78]
007760E5  8B D6                           mov edx, esi
007760E7  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
007760EB  48 8B C7                        mov rax, rdi
007760EE  E8 DD 49 F4 FF                  call 0x1406baad0
007760F3  8B D0                           mov edx, eax
007760F5  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
007760FA  8B D8                           mov ebx, eax
007760FC  E8 23 0B 00 00                  call 0x140776c24
00776101  85 DB                           test ebx, ebx
00776103  79 18                           jns 0x14077611d
00776105  41 83 C9 FF                     or r9d, 0xffffffff
00776109  48 8D 0D 90 DE 38 00            lea rcx, [rip + 0x38de90]
00776110  44 8B C3                        mov r8d, ebx
00776113  BA 88 09 00 00                  mov edx, 0x988
00776118  E8 7F 52 21 00                  call 0x14098b39c
0077611D  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00776122  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00776126  49 8B 6B 18                     mov rbp, qword ptr [r11 + 0x18]
0077612A  49 8B 73 20                     mov rsi, qword ptr [r11 + 0x20]
0077612E  49 8B E3                        mov rsp, r11
00776131  5F                              pop rdi
00776132  C3                              ret
00776133  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmpCallSetDisplayState(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (96);
    if (*(unsigned __int64 *)(a2 + 56) == 0) goto loc_0077611D;
    result = 0;
    v_stack_m40 = a3;
    *(unsigned __int64 *)(v_rsp - 72) = *(unsigned __int64 *)(a2 + 56);
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = TtmpStartCallout(v_rsp - 56, a1, a2, result + 4);
    result = guard_dispatch_icall(*(unsigned __int64 *)(a2 + 24), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)(*(unsigned int *)(a1 + 120)), result + 4);
    result = TtmpStopCallout(v_stack_m38, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(a1 + 120)), result + 4);
    if (sign_flag) {
        a4 = (unsigned int)((result + 4) | (0xFFFFFFFFULL));
        a1 = v_rip + 3726992;
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a2 = 0x988ULL;
        result = TtmiLogError(a1, a2, a3, a4);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmpCallSetDisplayState(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (96);
    if (*(uint64_t *)(arg2 + 0x38) == 0) goto loc_0077611D;
    result = 0;
    v_stack_m40 = Arg3;
    *(uint64_t *)(local_rsp - 0x48) = *(uint64_t *)(arg2 + 0x38);
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = TtmpStartCallout(local_rsp - 56, Arg1, Arg2, result + 4);
    result = guard_dispatch_icall(*(uint64_t *)(arg2 + 0x18), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)(*(uint32_t *)(arg1 + 0x78)), result + 4);
    result = TtmpStopCallout(v_stack_m38, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(arg1 + 0x78)), result + 4);
    if (sign_flag) {
        a4 = (uint32_t)((result + 4) | (0xFFFFFFFFULL));
        Arg1 = v_rip + 3726992;
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg2 = 0x988ULL;
        result = TtmiLogError(Arg1, Arg2, Arg3, a4);
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077608C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077608C[BB_0077608C]
  bb_007760B2[BB_007760B2]
  bb_00776105[BB_00776105]
  bb_0077611D[BB_0077611D]
  bb_00776133[BB_00776133]
  bb_0077608C -->|branch| bb_0077611D
  bb_0077608C -->|fallthrough| bb_007760B2
  bb_007760B2 -->|branch| bb_0077611D
  bb_007760B2 -->|fallthrough| bb_00776105
  bb_00776105 -->|flow| bb_0077611D
```
