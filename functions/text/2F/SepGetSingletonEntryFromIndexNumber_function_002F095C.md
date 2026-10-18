# SepGetSingletonEntryFromIndexNumber

- RVA: `0x002F095C`–`0x002F09C0` (길이 `100` bytes)
- VA: `0x00000001402F095C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `29`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002F097B` → [ExAcquireSpinLockShared](../24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x002F09A7` → [ExReleaseSpinLockShared](ExReleaseSpinLockShared_function_002F0EF0.md) (function, `0x002F0EF0`)

### Direct callers
- [SepCleanupMarkedForDeletionEntries](../2E/SepCleanupMarkedForDeletionEntries_function_002EEC84.md) at `0x002EECDE`
- [SepInitSingletonEntry](../2E/SepInitSingletonEntry_function_002EEF64.md) at `0x002EEF71`
- [sub_003A7C07](../3A/Unknown_function_003A7C07.md) at `0x003A7C0E`
- [SepValidateAndCopyGlobalEntry](../4F/SepValidateAndCopyGlobalEntry_function_004F825C.md) at `0x004F82D9`
- [SepSetSingletonEntry](../60/SepSetSingletonEntry_function_00609DA0.md) at `0x00609DC1`

### Static image references
- `0x002F096F` → RVA `0x00E08960` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002F095C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002F0961  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
002F0966  57                              push rdi
002F0967  48 83 EC 20                     sub rsp, 0x20
002F096B  8B D9                           mov ebx, ecx
002F096D  8B F1                           mov esi, ecx
002F096F  48 8B 0D EA 7F B1 00            mov rcx, qword ptr [rip + 0xb17fea]
002F0976  33 FF                           xor edi, edi
002F0978  C1 EB 06                        shr ebx, 6
002F097B  E8 60 D3 F5 FF                  call 0x14024dce0
002F0980  48 8B 0D D9 7F B1 00            mov rcx, qword ptr [rip + 0xb17fd9]
002F0987  44 8A D0                        mov r10b, al
002F098A  3B 59 04                        cmp ebx, dword ptr [rcx + 4]
002F098D  73 15                           jae 0x1402f09a4
002F098F  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
002F0993  8B C6                           mov eax, esi
002F0995  83 E0 3F                        and eax, 0x3f
002F0998  48 8D 14 40                     lea rdx, [rax + rax*2]
002F099C  49 8B 04 D8                     mov rax, qword ptr [r8 + rbx*8]
002F09A0  48 8D 3C D0                     lea rdi, [rax + rdx*8]
002F09A4  41 8A D2                        mov dl, r10b
002F09A7  E8 44 05 00 00                  call 0x1402f0ef0
002F09AC  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002F09B1  48 8B C7                        mov rax, rdi
002F09B4  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
002F09B9  48 83 C4 20                     add rsp, 0x20
002F09BD  5F                              pop rdi
002F09BE  C3                              ret
002F09BF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepGetSingletonEntryFromIndexNumber(int a1)
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
    v_rdi = 0;
    v_rbx = (unsigned int)(((unsigned int)(a1)) >> (6));
    result = ExAcquireSpinLockShared(*(unsigned __int64 *)(v_rip + 11632618), a2, a3, a4);
    if (((unsigned int)(v_rbx)) < (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11632601) + 4))) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11632601) + 8);
        result = (unsigned int)((unsigned int)(a1));
        result = (unsigned int)((result) & (63));
        a2 = result + result * 2;
        result = *(unsigned __int64 *)(a3 + v_rbx * 8);
        v_rdi = result + a2 * 8;
    }
    result = ExReleaseSpinLockShared(*(unsigned __int64 *)(v_rip + 11632601), (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return v_rdi;
}
```

## 5. (Beta) C Style

```c
int64_t SepGetSingletonEntryFromIndexNumber(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    local_rbx = (uint32_t)(((uint32_t)(Arg1)) >> (6));
    result = ExAcquireSpinLockShared(*(uint64_t *)(v_rip + 0xB17FEA), a2, a3, a4);
    if (((uint32_t)(local_rbx)) < (*(uint32_t *)(*(uint64_t *)(v_rip + 0xB17FD9) + 0x4))) {
        a3 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB17FD9) + 0x8);
        result = (uint32_t)((uint32_t)(Arg1));
        result = (uint32_t)((result) & (63));
        a2 = result + result * 2;
        result = *(uint64_t *)(a3 + local_rbx * 8);
        local_rdi = result + a2 * 8;
    }
    result = ExReleaseSpinLockShared(*(uint64_t *)(v_rip + 0xB17FD9), (uint8_t)((uint8_t)(result)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return local_rdi;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F095C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002F095C[BB_002F095C]
  bb_002F098F[BB_002F098F]
  bb_002F09A4[BB_002F09A4]
  bb_002F09BF[BB_002F09BF]
  bb_002F095C -->|branch| bb_002F09A4
  bb_002F095C -->|fallthrough| bb_002F098F
  bb_002F098F -->|flow| bb_002F09A4
```
