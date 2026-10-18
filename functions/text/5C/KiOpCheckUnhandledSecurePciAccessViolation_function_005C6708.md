# KiOpCheckUnhandledSecurePciAccessViolation

- RVA: `0x005C6708`–`0x005C67BE` (길이 `182` bytes)
- VA: `0x00000001405C6708`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CAB00`
- 디코드: `53`개 명령, `182/182` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005C675A` → [KiOpGetPciConfigSpaceAccessInfoFromPhysicalAddress](../4C/KiOpGetPciConfigSpaceAccessInfoFromPhysicalAddress_function_004C23C0.md) (function, `0x004C23C0`)

### Direct callers
- [KiPreprocessFault](../3D/KiPreprocessFault_function_003D7E70.md) at `0x003D8168`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C6708  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
005C670D  55                              push rbp
005C670E  56                              push rsi
005C670F  57                              push rdi
005C6710  48 8B EC                        mov rbp, rsp
005C6713  48 83 EC 40                     sub rsp, 0x40
005C6717  33 F6                           xor esi, esi
005C6719  48 8B F9                        mov rdi, rcx
005C671C  48 8B 49 68                     mov rcx, qword ptr [rcx + 0x68]
005C6720  48 8B DA                        mov rbx, rdx
005C6723  89 75 F4                        mov dword ptr [rbp - 0xc], esi
005C6726  40 88 75 20                     mov byte ptr [rbp + 0x20], sil
005C672A  40 88 75 30                     mov byte ptr [rbp + 0x30], sil
005C672E  40 88 75 38                     mov byte ptr [rbp + 0x38], sil
005C6732  66 89 75 F0                     mov word ptr [rbp - 0x10], si
005C6736  48 83 F9 FF                     cmp rcx, -1
005C673A  74 74                           je 0x1405c67b0
005C673C  48 8D 45 F4                     lea rax, [rbp - 0xc]
005C6740  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005C6745  4C 8D 4D 30                     lea r9, [rbp + 0x30]
005C6749  48 8D 45 38                     lea rax, [rbp + 0x38]
005C674D  4C 8D 45 20                     lea r8, [rbp + 0x20]
005C6751  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005C6756  48 8D 55 F0                     lea rdx, [rbp - 0x10]
005C675A  E8 61 BC EF FF                  call 0x1404c23c0
005C675F  85 C0                           test eax, eax
005C6761  78 4D                           js 0x1405c67b0
005C6763  0F B7 4D F0                     movzx ecx, word ptr [rbp - 0x10]
005C6767  48 C1 E1 08                     shl rcx, 8
005C676B  C7 03 09 00 00 10               mov dword ptr [rbx], 0x10000009
005C6771  C7 43 18 04 00 00 00            mov dword ptr [rbx + 0x18], 4
005C6778  0F B6 47 38                     movzx eax, byte ptr [rdi + 0x38]
005C677C  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
005C6780  0F B6 45 20                     movzx eax, byte ptr [rbp + 0x20]
005C6784  48 0B C8                        or rcx, rax
005C6787  0F B6 45 30                     movzx eax, byte ptr [rbp + 0x30]
005C678B  48 C1 E1 05                     shl rcx, 5
005C678F  48 0B C8                        or rcx, rax
005C6792  0F B6 45 38                     movzx eax, byte ptr [rbp + 0x38]
005C6796  48 C1 E1 03                     shl rcx, 3
005C679A  48 0B C8                        or rcx, rax
005C679D  8B 45 F4                        mov eax, dword ptr [rbp - 0xc]
005C67A0  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
005C67A4  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
005C67A8  48 89 43 38                     mov qword ptr [rbx + 0x38], rax
005C67AC  48 89 4B 28                     mov qword ptr [rbx + 0x28], rcx
005C67B0  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
005C67B5  48 83 C4 40                     add rsp, 0x40
005C67B9  5F                              pop rdi
005C67BA  5E                              pop rsi
005C67BB  5D                              pop rbp
005C67BC  C3                              ret
005C67BD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiOpCheckUnhandledSecurePciAccessViolation(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m24;
    unsigned __int16 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (64);
    v_rsi = 0;
    v_stack_m24 = 0;
    v_stack_p8 = 0;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    v_stack_m28 = 0;
    if ((*(unsigned __int64 *)(a1 + 104)) == -1) goto loc_005C67B0;
    v_stack_m30 = v_stack_m24;
    v_stack_m38 = v_stack_p20;
    result = KiOpGetPciConfigSpaceAccessInfoFromPhysicalAddress(*(unsigned __int64 *)(a1 + 104), v_stack_m28, v_stack_p8, v_stack_p18);
    if (!(sign_flag)) {
        a1 = v_stack_m28;
        a1 = (a1) << (8);
        *(unsigned int *)(a2) = 0x10000009ULL;
        *(unsigned int *)(a2 + 24) = 4;
        result = *(unsigned __int8 *)(a1 + 56);
        *(unsigned __int64 *)(a2 + 32) = result;
        result = v_stack_p8;
        a1 = (a1) | (result);
        result = v_stack_p18;
        a1 = (a1) << (5);
        a1 = (a1) | (result);
        result = v_stack_p20;
        a1 = (a1) << (3);
        a1 = (a1) | (result);
        result = v_stack_m24;
        *(unsigned __int64 *)(a2 + 48) = result;
        result = *(unsigned __int64 *)(a2 + 16);
        *(unsigned __int64 *)(a2 + 56) = result;
        *(unsigned __int64 *)(a2 + 40) = a1;
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiOpCheckUnhandledSecurePciAccessViolation(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m24;
    uint16_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint8_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (64);
    local_rsi = 0;
    v_stack_m24 = 0;
    v_stack_p8 = 0;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    v_stack_m28 = 0;
    if ((*(uint64_t *)(arg1 + 0x68)) == -1) goto loc_005C67B0;
    v_stack_m30 = v_stack_m24;
    v_stack_m38 = v_stack_p20;
    result = KiOpGetPciConfigSpaceAccessInfoFromPhysicalAddress(*(uint64_t *)(arg1 + 0x68), v_stack_m28, v_stack_p8, v_stack_p18);
    if (!(sign_flag)) {
        Arg1 = v_stack_m28;
        Arg1 = (Arg1) << (8);
        *(uint32_t *)(arg2) = 0x10000009ULL;
        *(uint32_t *)(arg2 + 0x18) = 4;
        result = *(uint8_t *)(arg1 + 0x38);
        *(uint64_t *)(arg2 + 0x20) = result;
        result = v_stack_p8;
        Arg1 = (Arg1) | (result);
        result = v_stack_p18;
        Arg1 = (Arg1) << (5);
        Arg1 = (Arg1) | (result);
        result = v_stack_p20;
        Arg1 = (Arg1) << (3);
        Arg1 = (Arg1) | (result);
        result = v_stack_m24;
        *(uint64_t *)(arg2 + 0x30) = result;
        result = *(uint64_t *)(arg2 + 0x10);
        *(uint64_t *)(arg2 + 0x38) = result;
        *(void **)(arg2 + 0x28) = Arg1;
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `8` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `32` | `W` |
| `Arg2` | `+ 0x20` | `64` | `W` |
| `Arg2` | `+ 0x28` | `64` | `W` |
| `Arg2` | `+ 0x30` | `64` | `W` |
| `Arg2` | `+ 0x38` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C6708&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005C6708[BB_005C6708]
  bb_005C673C[BB_005C673C]
  bb_005C6763[BB_005C6763]
  bb_005C67B0[BB_005C67B0]
  bb_005C67BD[BB_005C67BD]
  bb_005C6708 -->|branch| bb_005C67B0
  bb_005C6708 -->|fallthrough| bb_005C673C
  bb_005C673C -->|branch| bb_005C67B0
  bb_005C673C -->|fallthrough| bb_005C6763
  bb_005C6763 -->|flow| bb_005C67B0
```
