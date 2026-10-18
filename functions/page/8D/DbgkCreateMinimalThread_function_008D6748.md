# DbgkCreateMinimalThread

- RVA: `0x008D6748`–`0x008D67F1` (길이 `169` bytes)
- VA: `0x00000001408D6748`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000852C8`
- 디코드: `35`개 명령, `169/169` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008D6777` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008D6798` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008D67CA` → [DbgkpSendApiMessage](../A7/DbgkpSendApiMessage_function_00A79458.md) (function, `0x00A79458`)
- `0x008D67DA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PspUserThreadStartup](PspUserThreadStartup_function_008D5B10.md) at `0x008D5BD5`

### Static image references
- `0x008D6755` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008D6777` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008D6798` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008D67DA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008D6748  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
008D674D  57                              push rdi
008D674E  48 81 EC 40 01 00 00            sub rsp, 0x140
008D6755  48 8B 05 E4 3F 53 00            mov rax, qword ptr [rip + 0x533fe4]
008D675C  48 33 C4                        xor rax, rsp
008D675F  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
008D6767  48 8B D9                        mov rbx, rcx
008D676A  33 D2                           xor edx, edx
008D676C  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
008D6771  41 B8 D0 00 00 00               mov r8d, 0xd0
008D6777  E8 C4 04 DF FF                  call 0x1406c6c40
008D677C  48 8B BB B8 00 00 00            mov rdi, qword ptr [rbx + 0xb8]
008D6783  48 83 BF 08 03 00 00 00         cmp qword ptr [rdi + 0x308], 0
008D678B  74 42                           je 0x1408d67cf
008D678D  33 D2                           xor edx, edx
008D678F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
008D6794  44 8D 42 40                     lea r8d, [rdx + 0x40]
008D6798  E8 A3 04 DF FF                  call 0x1406c6c40
008D679D  48 8B 83 60 05 00 00            mov rax, qword ptr [rbx + 0x560]
008D67A4  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
008D67A9  BA 01 00 00 00                  mov edx, 1
008D67AE  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008D67B3  48 8B CF                        mov rcx, rdi
008D67B6  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
008D67BA  C7 44 24 20 18 00 40 00         mov dword ptr [rsp + 0x20], 0x400018
008D67C2  C7 44 24 24 08 00 00 00         mov dword ptr [rsp + 0x24], 8
008D67CA  E8 89 2C 1A 00                  call 0x140a79458
008D67CF  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
008D67D7  48 33 CC                        xor rcx, rsp
008D67DA  E8 61 5E DD FF                  call 0x1406ac640
008D67DF  48 8B 9C 24 58 01 00 00         mov rbx, qword ptr [rsp + 0x158]
008D67E7  48 81 C4 40 01 00 00            add rsp, 0x140
008D67EE  5F                              pop rdi
008D67EF  C3                              ret
008D67F0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DbgkCreateMinimalThread(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m124;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 5455844)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_mE8, a2, 208, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 776)) != 0) {
        a2 = 0;
        a1 = v_stack_m128;
        a3 = a2 + 64;
        result = memset(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(a1 + 1376);
        a3 = v_stack_m128;
        a2 = 1;
        v_stack_mF0 = result;
        a1 = *(unsigned __int64 *)(a1 + 184);
        v_stack_m100 = a2;
        v_stack_m128 = 0x400018ULL;
        v_stack_m124 = 8;
        result = DbgkpSendApiMessage(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (320);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DbgkCreateMinimalThread(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m124;
    uint64_t v_stack_m128;
    uint64_t v_stack_m18;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0x533FE4)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, 208, a4);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x308)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m128;
        a3 = Arg2 + 64;
        result = memset(Arg1, Arg2, a3, a4);
        result = *(uint64_t *)(arg1 + 0x560);
        a3 = v_stack_m128;
        Arg2 = 1;
        v_stack_mF0 = result;
        Arg1 = *(uint64_t *)(arg1 + 0xB8);
        v_stack_m100 = Arg2;
        v_stack_m128 = 0x400018ULL;
        v_stack_m124 = 8;
        result = DbgkpSendApiMessage(Arg1, Arg2, a3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (320);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0x560` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008D6748&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008D6748[BB_008D6748]
  bb_008D678D[BB_008D678D]
  bb_008D67CF[BB_008D67CF]
  bb_008D67F0[BB_008D67F0]
  bb_008D6748 -->|branch| bb_008D67CF
  bb_008D6748 -->|fallthrough| bb_008D678D
  bb_008D678D -->|flow| bb_008D67CF
```
