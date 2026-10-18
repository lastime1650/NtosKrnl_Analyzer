# PspQueryJobIoAttribution

- RVA: `0x009FC648`–`0x009FC6EB` (길이 `163` bytes)
- VA: `0x00000001409FC648`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A716C`
- 디코드: `44`개 명령, `163/163` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009FC68C` → [IoDiskIoAttributionQuery](../../text/37/IoDiskIoAttributionQuery_function_00379D38.md) (function, `0x00379D38`)

### Direct callers
- [NtQueryInformationJobObject](NtQueryInformationJobObject_function_009FB860.md) at `0x009FC290`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009FC68C` → [IoDiskIoAttributionQuery](../../text/37/IoDiskIoAttributionQuery_function_00379D38.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009FC648  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009FC64D  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
009FC652  55                              push rbp
009FC653  48 8B EC                        mov rbp, rsp
009FC656  48 83 EC 60                     sub rsp, 0x60
009FC65A  0F 57 C0                        xorps xmm0, xmm0
009FC65D  0F 57 C9                        xorps xmm1, xmm1
009FC660  33 DB                           xor ebx, ebx
009FC662  48 8B FA                        mov rdi, rdx
009FC665  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
009FC669  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
009FC66D  0F 11 4D E0                     movups xmmword ptr [rbp - 0x20], xmm1
009FC671  0F 11 4D F0                     movups xmmword ptr [rbp - 0x10], xmm1
009FC675  39 99 28 06 00 00               cmp dword ptr [rcx + 0x628], ebx
009FC67B  74 67                           je 0x1409fc6e4
009FC67D  48 8B 89 30 06 00 00            mov rcx, qword ptr [rcx + 0x630]
009FC684  4C 8D 45 E0                     lea r8, [rbp - 0x20]
009FC688  48 8D 55 C0                     lea rdx, [rbp - 0x40]
009FC68C  E8 A7 D6 97 FF                  call 0x140379d38
009FC691  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
009FC695  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
009FC699  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
009FC69D  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
009FC6A1  48 89 4F 20                     mov qword ptr [rdi + 0x20], rcx
009FC6A5  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
009FC6A9  48 89 4F 28                     mov qword ptr [rdi + 0x28], rcx
009FC6AD  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
009FC6B1  48 89 4F 30                     mov qword ptr [rdi + 0x30], rcx
009FC6B5  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
009FC6B9  48 89 4F 38                     mov qword ptr [rdi + 0x38], rcx
009FC6BD  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
009FC6C1  48 89 47 08                     mov qword ptr [rdi + 8], rax
009FC6C5  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
009FC6C9  48 89 4F 40                     mov qword ptr [rdi + 0x40], rcx
009FC6CD  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
009FC6D1  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
009FC6D6  8B C3                           mov eax, ebx
009FC6D8  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
009FC6DD  48 83 C4 60                     add rsp, 0x60
009FC6E1  5D                              pop rbp
009FC6E2  C3                              ret
009FC6E3  CC                              int3
009FC6E4  BB 25 02 00 C0                  mov ebx, 0xc0000225
009FC6E9  EB E6                           jmp 0x1409fc6d1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspQueryJobIoAttribution(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    v_rsp = (v_rsp) - (96);
    v_rbx = 0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm1;
    v_stack_m18 = v_xmm1;
    if ((*(unsigned int *)(a1 + 1576)) == 0) goto loc_009FC6E4;
    result = IoDiskIoAttributionQuery(*(unsigned __int64 *)(a1 + 1584), v_stack_m48, v_stack_m28, a4);
    *(unsigned __int64 *)(a2 + 24) = v_stack_m40;
    *(unsigned __int64 *)(a2 + 32) = v_stack_m38;
    *(unsigned __int64 *)(a2 + 40) = v_stack_m10;
    *(unsigned __int64 *)(a2 + 48) = v_stack_m28;
    *(unsigned __int64 *)(a2 + 56) = v_stack_m20;
    *(unsigned __int64 *)(a2 + 8) = v_stack_m30;
    *(unsigned __int64 *)(a2 + 64) = v_stack_m18;
    *(unsigned __int64 *)(a2 + 16) = v_stack_m48;
loc_009FC6D1:
    v_rsp = (v_rsp) + (96);
    return 0;
loc_009FC6E4:
    goto loc_009FC6D1;
}
```

## 5. (Beta) C Style

```c
int64_t PspQueryJobIoAttribution(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    local_rsp = (local_rsp) - (96);
    local_rbx = 0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm1;
    v_stack_m18 = v_xmm1;
    if ((*(uint32_t *)(arg1 + 0x628)) == 0) goto loc_009FC6E4;
    result = IoDiskIoAttributionQuery(*(uint64_t *)(arg1 + 0x630), v_stack_m48, v_stack_m28, a4);
    *(uint64_t *)(arg2 + 0x18) = v_stack_m40;
    *(uint64_t *)(arg2 + 0x20) = v_stack_m38;
    *(uint64_t *)(arg2 + 0x28) = v_stack_m10;
    *(uint64_t *)(arg2 + 0x30) = v_stack_m28;
    *(uint64_t *)(arg2 + 0x38) = v_stack_m20;
    *(uint64_t *)(arg2 + 0x8) = v_stack_m30;
    *(uint64_t *)(arg2 + 0x40) = v_stack_m18;
    *(uint64_t *)(arg2 + 0x10) = v_stack_m48;
loc_009FC6D1:
    local_rsp = (local_rsp) + (96);
    return 0;
loc_009FC6E4:
    goto loc_009FC6D1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x628` | `32` | `R` |
| `Arg1` | `+ 0x630` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x10` | `64` | `W` |
| `Arg2` | `+ 0x18` | `64` | `W` |
| `Arg2` | `+ 0x20` | `64` | `W` |
| `Arg2` | `+ 0x28` | `64` | `W` |
| `Arg2` | `+ 0x30` | `64` | `W` |
| `Arg2` | `+ 0x38` | `64` | `W` |
| `Arg2` | `+ 0x40` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009FC648&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009FC648[BB_009FC648]
  bb_009FC67D[BB_009FC67D]
  bb_009FC6D1[BB_009FC6D1]
  bb_009FC6E3[BB_009FC6E3]
  bb_009FC6E4[BB_009FC6E4]
  bb_009FC648 -->|branch| bb_009FC6E4
  bb_009FC648 -->|fallthrough| bb_009FC67D
  bb_009FC67D -->|flow| bb_009FC6D1
  bb_009FC6E3 -->|flow| bb_009FC6E4
  bb_009FC6E4 -->|branch| bb_009FC6D1
```
