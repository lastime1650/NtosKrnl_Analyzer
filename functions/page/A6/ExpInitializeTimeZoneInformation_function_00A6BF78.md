# ExpInitializeTimeZoneInformation

- RVA: `0x00A6BF78`–`0x00A6C020` (길이 `168` bytes)
- VA: `0x0000000140A6BF78`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5F8`
- 디코드: `34`개 명령, `168/168` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00A6BF9E` → [ExpInitializeTimeChangeWorker](ExpInitializeTimeChangeWorker_function_00A6C474.md) (function, `0x00A6C474`)
- `0x00A6BFB9` → [ExpInitializeTimeChangeWorker](ExpInitializeTimeChangeWorker_function_00A6C474.md) (function, `0x00A6C474`)
- `0x00A6BFD4` → [ExpInitializeTimeChangeWorker](ExpInitializeTimeChangeWorker_function_00A6C474.md) (function, `0x00A6C474`)

### Direct callers
- [ExpRefreshTimeZoneInformation](ExpRefreshTimeZoneInformation_function_00A6B46C.md) at `0x00A6B501`

### Static image references
- `0x00A6BF97` → RVA `0x00655710` (`ExpTimeZoneDpcRoutine`; read)
- `0x00A6BFB2` → RVA `0x006555A0` (`ExpNextYearDpcRoutine`; read)
- `0x00A6BFCD` → RVA `0x00223520` (`ExpCenturyDpcRoutine`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A6BF78  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A6BF7D  57                              push rdi
00A6BF7E  48 83 EC 30                     sub rsp, 0x30
00A6BF82  48 8B D9                        mov rbx, rcx
00A6BF85  48 8B FA                        mov rdi, rdx
00A6BF88  48 8D 8A C0 01 00 00            lea rcx, [rdx + 0x1c0]
00A6BF8F  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A6BF94  4C 8B C3                        mov r8, rbx
00A6BF97  48 8D 15 72 97 BE FF            lea rdx, [rip - 0x41688e]
00A6BF9E  E8 D1 04 00 00                  call 0x140a6c474
00A6BFA3  48 8D 8F 00 03 00 00            lea rcx, [rdi + 0x300]
00A6BFAA  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A6BFAF  4C 8B C3                        mov r8, rbx
00A6BFB2  48 8D 15 E7 95 BE FF            lea rdx, [rip - 0x416a19]
00A6BFB9  E8 B6 04 00 00                  call 0x140a6c474
00A6BFBE  48 8D 8F 60 02 00 00            lea rcx, [rdi + 0x260]
00A6BFC5  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A6BFCA  4C 8B C3                        mov r8, rbx
00A6BFCD  48 8D 15 4C 75 7B FF            lea rdx, [rip - 0x848ab4]
00A6BFD4  E8 9B 04 00 00                  call 0x140a6c474
00A6BFD9  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00A6BFDE  B8 01 00 00 00                  mov eax, 1
00A6BFE3  0F 57 C0                        xorps xmm0, xmm0
00A6BFE6  0F 57 C9                        xorps xmm1, xmm1
00A6BFE9  0F 11 87 B0 03 00 00            movups xmmword ptr [rdi + 0x3b0], xmm0
00A6BFF0  0F 11 8F C8 03 00 00            movups xmmword ptr [rdi + 0x3c8], xmm1
00A6BFF7  C7 87 B2 03 00 00 01 00 01 00   mov dword ptr [rdi + 0x3b2], 0x10001
00A6C001  66 89 87 BC 03 00 00            mov word ptr [rdi + 0x3bc], ax
00A6C008  C7 87 CA 03 00 00 01 00 01 00   mov dword ptr [rdi + 0x3ca], 0x10001
00A6C012  66 89 87 D4 03 00 00            mov word ptr [rdi + 0x3d4], ax
00A6C019  48 83 C4 30                     add rsp, 0x30
00A6C01D  5F                              pop rdi
00A6C01E  C3                              ret
00A6C01F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpInitializeTimeZoneInformation(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_stack_m18 = a1;
    result = ExpInitializeTimeChangeWorker(a2 + 448, v_rip - 4286606, a1, a4);
    v_stack_m18 = a1;
    result = ExpInitializeTimeChangeWorker(a2 + 768, v_rip - 4287001, a1, a4);
    v_stack_m18 = a1;
    result = ExpInitializeTimeChangeWorker(a2 + 608, v_rip - 8686260, a1, a4);
    *(unsigned __int64 *)(a2 + 944) = v_xmm0;
    *(unsigned __int64 *)(a2 + 968) = v_xmm1;
    *(unsigned int *)(a2 + 946) = 0x10001ULL;
    *(unsigned __int16 *)(a2 + 956) = 1;
    *(unsigned int *)(a2 + 970) = 0x10001ULL;
    *(unsigned __int16 *)(a2 + 980) = 1;
    v_rsp = (v_rsp) + (48);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t ExpInitializeTimeZoneInformation(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    v_stack_m18 = Arg1;
    result = ExpInitializeTimeChangeWorker(Arg2 + 448, v_rip - 4286606, Arg1, a4);
    v_stack_m18 = Arg1;
    result = ExpInitializeTimeChangeWorker(Arg2 + 768, v_rip - 4287001, Arg1, a4);
    v_stack_m18 = Arg1;
    result = ExpInitializeTimeChangeWorker(Arg2 + 608, v_rip - 8686260, Arg1, a4);
    *(uint64_t *)(arg2 + 0x3B0) = v_xmm0;
    *(uint64_t *)(arg2 + 0x3C8) = v_xmm1;
    *(uint32_t *)(arg2 + 0x3B2) = 0x10001ULL;
    *(uint16_t *)(arg2 + 0x3BC) = 1;
    *(uint32_t *)(arg2 + 0x3CA) = 0x10001ULL;
    *(uint16_t *)(arg2 + 0x3D4) = 1;
    local_rsp = (local_rsp) + (48);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x1C0` | `64` | `R` |
| `Arg2` | `+ 0x260` | `64` | `R` |
| `Arg2` | `+ 0x300` | `64` | `R` |
| `Arg2` | `+ 0x3B0` | `128` | `R` |
| `Arg2` | `+ 0x3B2` | `32` | `W` |
| `Arg2` | `+ 0x3BC` | `16` | `W` |
| `Arg2` | `+ 0x3C8` | `128` | `R` |
| `Arg2` | `+ 0x3CA` | `32` | `W` |
| `Arg2` | `+ 0x3D4` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A6BF78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A6BF78[BB_00A6BF78]
  bb_00A6C01F[BB_00A6C01F]
```
