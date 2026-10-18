# PspMarkSessionReferenceProcess

- RVA: `0x00789220`–`0x007892A2` (길이 `130` bytes)
- VA: `0x0000000140789220`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `31`개 명령, `130/130` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00789253` → [PspLockProcessListExclusive](../../text/22/PspLockProcessListExclusive_function_0022578C.md) (function, `0x0022578C`)
- `0x0078928C` → [PspUnlockProcessListExclusive](../../text/2D/PspUnlockProcessListExclusive_function_002DFD18.md) (function, `0x002DFD18`)

### Direct callers
- [PsSessionCreate](../70/PsSessionCreate_function_00700438.md) at `0x00700520`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00789253` → [PspLockProcessListExclusive](../../text/22/PspLockProcessListExclusive_function_0022578C.md) (`PAGE` → `.text`)
  - `0x0078928C` → [PspUnlockProcessListExclusive](../../text/2D/PspUnlockProcessListExclusive_function_002DFD18.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00789220  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00789225  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0078922A  57                              push rdi
0078922B  48 83 EC 20                     sub rsp, 0x20
0078922F  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
00789238  48 8B FA                        mov rdi, rdx
0078923B  48 89 91 E8 02 00 00            mov qword ptr [rcx + 0x2e8], rdx
00789242  48 8B D9                        mov rbx, rcx
00789245  F0 81 89 F4 01 00 00 00 00 01 00  lock or dword ptr [rcx + 0x1f4], 0x10000
00789250  48 8B CE                        mov rcx, rsi
00789253  E8 34 C5 A9 FF                  call 0x14022578c
00789258  F0 83 8B DC 07 00 00 08         lock or dword ptr [rbx + 0x7dc], 8
00789260  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00789264  48 83 C7 10                     add rdi, 0x10
00789268  48 81 C3 30 02 00 00            add rbx, 0x230
0078926F  48 39 38                        cmp qword ptr [rax], rdi
00789272  74 07                           je 0x14078927b
00789274  B9 03 00 00 00                  mov ecx, 3
00789279  CD 29                           int 0x29
0078927B  48 89 3B                        mov qword ptr [rbx], rdi
0078927E  48 8B CE                        mov rcx, rsi
00789281  48 89 43 08                     mov qword ptr [rbx + 8], rax
00789285  48 89 18                        mov qword ptr [rax], rbx
00789288  48 89 5F 08                     mov qword ptr [rdi + 8], rbx
0078928C  E8 87 6A B5 FF                  call 0x1402dfd18
00789291  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00789296  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0078929B  48 83 C4 20                     add rsp, 0x20
0078929F  5F                              pop rdi
007892A0  C3                              ret
007892A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspMarkSessionReferenceProcess(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    *(unsigned __int64 *)(a1 + 744) = a2;
    result = PspLockProcessListExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_rdi = (a2) + (16);
    v_rbx = (a1) + (560);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24))) != v_rdi) {
        a1 = 3;
    }
    *(unsigned __int64 *)(v_rbx) = v_rdi;
    *(unsigned __int64 *)(v_rbx + 8) = *(unsigned __int64 *)(a2 + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24)) = v_rbx;
    *(unsigned __int64 *)(v_rdi + 8) = v_rbx;
    result = PspUnlockProcessListExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspMarkSessionReferenceProcess(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    *(void **)(arg1 + 0x2E8) = Arg2;
    result = PspLockProcessListExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, a4);
    local_rdi = (Arg2) + (16);
    local_rbx = (Arg1) + (560);
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x18))) != local_rdi) {
        Arg1 = 3;
    }
    *(uint64_t *)(local_rbx) = local_rdi;
    *(uint64_t *)(local_rbx + 0x8) = *(uint64_t *)(arg2 + 0x18);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x18)) = local_rbx;
    *(uint64_t *)(local_rdi + 0x8) = local_rbx;
    result = PspUnlockProcessListExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x1F4` | `32` | `R/W` |
| `Arg1` | `+ 0x2E8` | `64` | `W` |
| `Arg1` | `+ 0x7DC` | `32` | `R/W` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00789220&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00789220[BB_00789220]
  bb_00789274[BB_00789274]
  bb_0078927B[BB_0078927B]
  bb_007892A1[BB_007892A1]
  bb_00789220 -->|branch| bb_0078927B
  bb_00789220 -->|fallthrough| bb_00789274
  bb_00789274 -->|flow| bb_0078927B
```
