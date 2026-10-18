# KeQueryPrimaryGroupAffinityThread

- RVA: `0x003C7238`–`0x003C72AA` (길이 `114` bytes)
- VA: `0x00000001403C7238`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005FD94`
- 디코드: `30`개 명령, `114/114` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003C7262` → [KiAcquireThreadLockRaiseToDpc](../39/KiAcquireThreadLockRaiseToDpc_function_00396280.md) (function, `0x00396280`)
- `0x003C7294` → [KiReleaseThreadLockLowerIrql](KiReleaseThreadLockLowerIrql_function_003C65D0.md) (function, `0x003C65D0`)

### Direct callers
- [NtGetCurrentProcessorNumber](../../page/A9/NtGetCurrentProcessorNumber_function_00A95550.md) at `0x00A95583`
- [NtQueryInformationThread](../../page/AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4B1E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C7238  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003C723D  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
003C7242  57                              push rdi
003C7243  48 83 EC 20                     sub rsp, 0x20
003C7247  33 C0                           xor eax, eax
003C7249  48 8B F2                        mov rsi, rdx
003C724C  89 42 0A                        mov dword ptr [rdx + 0xa], eax
003C724F  33 FF                           xor edi, edi
003C7251  66 89 42 0E                     mov word ptr [rdx + 0xe], ax
003C7255  48 8B D9                        mov rbx, rcx
003C7258  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
003C725D  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
003C7262  E8 19 F0 FC FF                  call 0x140396280
003C7267  0F B7 83 48 02 00 00            movzx eax, word ptr [rbx + 0x248]
003C726E  66 89 46 08                     mov word ptr [rsi + 8], ax
003C7272  48 8B 8B 40 02 00 00            mov rcx, qword ptr [rbx + 0x240]
003C7279  0F B7 83 48 02 00 00            movzx eax, word ptr [rbx + 0x248]
003C7280  66 3B 01                        cmp ax, word ptr [rcx]
003C7283  73 05                           jae 0x1403c728a
003C7285  48 8B 7C C1 08                  mov rdi, qword ptr [rcx + rax*8 + 8]
003C728A  8A 54 24 30                     mov dl, byte ptr [rsp + 0x30]
003C728E  48 8B CB                        mov rcx, rbx
003C7291  48 89 3E                        mov qword ptr [rsi], rdi
003C7294  E8 37 F3 FF FF                  call 0x1403c65d0
003C7299  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
003C729E  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
003C72A3  48 83 C4 20                     add rsp, 0x20
003C72A7  5F                              pop rdi
003C72A8  C3                              ret
003C72A9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeQueryPrimaryGroupAffinityThread(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = 0;
    *(unsigned int *)(a2 + 10) = 0;
    v_rdi = 0;
    *(unsigned __int16 *)(a2 + 14) = 0;
    v_stack_p8 = 0;
    result = KiAcquireThreadLockRaiseToDpc(a1, v_stack_p8, a3, a4);
    *(unsigned __int16 *)(a2 + 8) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 584));
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 584))) < (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 576)))) {
        v_rdi = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 576) + *(unsigned __int16 *)(a1 + 584) * 8 + 8);
    }
    *(unsigned __int64 *)(a2) = v_rdi;
    result = KiReleaseThreadLockLowerIrql(a1, v_stack_p8, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeQueryPrimaryGroupAffinityThread(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = 0;
    *(uint32_t *)(arg2 + 0xA) = 0;
    local_rdi = 0;
    *(uint16_t *)(arg2 + 0xE) = 0;
    v_stack_p8 = 0;
    result = KiAcquireThreadLockRaiseToDpc(Arg1, v_stack_p8, a3, a4);
    *(uint16_t *)(arg2 + 0x8) = (uint16_t)(*(uint16_t *)(arg1 + 0x248));
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x248))) < (*(uint16_t *)(*(uint64_t *)(arg1 + 0x240)))) {
        local_rdi = *(uint64_t *)(*(uint64_t *)(arg1 + 0x240) + *(uint16_t *)(arg1 + 0x248) * 8 + 0x8);
    }
    *(uint64_t *)(arg2) = local_rdi;
    result = KiReleaseThreadLockLowerIrql(Arg1, v_stack_p8, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x240` | `64` | `R` |
| `Arg1` | `+ 0x248` | `16` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `16` | `W` |
| `Arg2` | `+ 0xA` | `32` | `W` |
| `Arg2` | `+ 0xE` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C7238&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003C7238[BB_003C7238]
  bb_003C7285[BB_003C7285]
  bb_003C728A[BB_003C728A]
  bb_003C72A9[BB_003C72A9]
  bb_003C7238 -->|branch| bb_003C728A
  bb_003C7238 -->|fallthrough| bb_003C7285
  bb_003C7285 -->|flow| bb_003C728A
```
