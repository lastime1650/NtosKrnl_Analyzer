# MiDereferenceAnyActiveHugeContext

- RVA: `0x002CB928`–`0x002CB9A3` (길이 `123` bytes)
- VA: `0x00000001402CB928`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F318`
- 디코드: `30`개 명령, `123/123` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002CB984` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x002CB98E` → [MiDereferenceHugeContext](../4D/MiDereferenceHugeContext_function_004D9664.md) (function, `0x004D9664`)
- `0x002CB99C` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- [MiBackgroundZeroNodePages](MiBackgroundZeroNodePages_function_002CB9B0.md) at `0x002CBA70`
- [MiDeleteZeroThreadContext](../4D/MiDeleteZeroThreadContext_function_004DF788.md) at `0x004DF7A1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002CB928  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002CB92D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
002CB932  57                              push rdi
002CB933  48 83 EC 20                     sub rsp, 0x20
002CB937  48 8B F1                        mov rsi, rcx
002CB93A  48 8B 89 48 02 00 00            mov rcx, qword ptr [rcx + 0x248]
002CB941  48 85 C9                        test rcx, rcx
002CB944  75 11                           jne 0x1402cb957
002CB946  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002CB94B  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
002CB950  48 83 C4 20                     add rsp, 0x20
002CB954  5F                              pop rdi
002CB955  C3                              ret
002CB956  CC                              int3
002CB957  48 8B 86 50 01 00 00            mov rax, qword ptr [rsi + 0x150]
002CB95E  48 8B 90 B0 00 00 00            mov rdx, qword ptr [rax + 0xb0]
002CB965  8B 81 38 02 00 00               mov eax, dword ptr [rcx + 0x238]
002CB96B  4C 8B 42 30                     mov r8, qword ptr [rdx + 0x30]
002CB96F  48 69 D0 80 DF 00 00            imul rdx, rax, 0xdf80
002CB976  49 8B 78 10                     mov rdi, qword ptr [r8 + 0x10]
002CB97A  48 03 FA                        add rdi, rdx
002CB97D  48 8D 8F 78 3B 00 00            lea rcx, [rdi + 0x3b78]
002CB984  E8 07 CD F7 FF                  call 0x140248690
002CB989  48 8B CE                        mov rcx, rsi
002CB98C  8A D8                           mov bl, al
002CB98E  E8 D1 DC 20 00                  call 0x1404d9664
002CB993  8A D3                           mov dl, bl
002CB995  48 8D 8F 78 3B 00 00            lea rcx, [rdi + 0x3b78]
002CB99C  E8 1F C9 F7 FF                  call 0x1402482c0
002CB9A1  EB A3                           jmp 0x1402cb946
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDereferenceAnyActiveHugeContext(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 584) != 0) goto loc_002CB957;
loc_002CB946:
    v_rsp = (v_rsp) + (32);
    return result;
loc_002CB957:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336) + 176)) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 584) + 568)));
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336) + 176) + 48) + 16)) + (a2);
    result = ExAcquireSpinLockExclusive(v_rdi + 15224, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336) + 176) + 48), a4);
    result = MiDereferenceHugeContext(v_stack_p10, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336) + 176) + 48), a4);
    result = MiReleaseSpinLockExclusive(v_rdi + 15224, (unsigned __int8)((unsigned __int8)(result)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336) + 176) + 48), a4);
    goto loc_002CB946;
}
```

## 5. (Beta) C Style

```c
int64_t MiDereferenceAnyActiveHugeContext(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x248) != 0) goto loc_002CB957;
loc_002CB946:
    local_rsp = (local_rsp) + (32);
    return result;
loc_002CB957:
    a2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150) + 0xB0)) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x248) + 0x238)));
    local_rdi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150) + 0xB0) + 0x30) + 0x10)) + (a2);
    result = ExAcquireSpinLockExclusive(local_rdi + 15224, a2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150) + 0xB0) + 0x30), a4);
    result = MiDereferenceHugeContext(v_stack_p10, a2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150) + 0xB0) + 0x30), a4);
    result = MiReleaseSpinLockExclusive(local_rdi + 15224, (uint8_t)((uint8_t)(result)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150) + 0xB0) + 0x30), a4);
    goto loc_002CB946;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x150` | `64` | `R` |
| `Arg1` | `+ 0x248` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002CB928&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002CB928[BB_002CB928]
  bb_002CB946[BB_002CB946]
  bb_002CB956[BB_002CB956]
  bb_002CB957[BB_002CB957]
  bb_002CB928 -->|branch| bb_002CB957
  bb_002CB928 -->|fallthrough| bb_002CB946
  bb_002CB956 -->|flow| bb_002CB957
  bb_002CB957 -->|branch| bb_002CB946
```
