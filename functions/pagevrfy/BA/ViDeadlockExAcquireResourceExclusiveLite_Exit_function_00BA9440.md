# ViDeadlockExAcquireResourceExclusiveLite_Exit

- RVA: `0x00BA9440`–`0x00BA947A` (길이 `58` bytes)
- VA: `0x0000000140BA9440`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `15`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA946F` → [VfDeadlockAcquireResource](../BB/VfDeadlockAcquireResource_function_00BB83B4.md) (function, `0x00BB83B4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA9440  48 83 EC 38                     sub rsp, 0x38
00BA9444  45 33 C9                        xor r9d, r9d
00BA9447  44 38 49 18                     cmp byte ptr [rcx + 0x18], r9b
00BA944B  74 27                           je 0x140ba9474
00BA944D  44 38 49 08                     cmp byte ptr [rcx + 8], r9b
00BA9451  BA 08 00 00 00                  mov edx, 8
00BA9456  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
00BA945F  48 8B 01                        mov rax, qword ptr [rcx]
00BA9462  41 0F 94 C1                     sete r9b
00BA9466  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00BA946A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BA946F  E8 40 EF 00 00                  call 0x140bb83b4
00BA9474  48 83 C4 38                     add rsp, 0x38
00BA9478  C3                              ret
00BA9479  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViDeadlockExAcquireResourceExclusiveLite_Exit(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a4 = 0;
    if ((*(unsigned __int8 *)(a1 + 24)) != 0) {
        a2 = 8;
        a3 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = *(unsigned __int64 *)(a1);
        a4 = ((*(unsigned __int8 *)(a1 + 8)) == 0) ? 1 : 0;
        a1 = *(unsigned __int64 *)(a1 + 16);
        v_stack_m18 = result;
        result = VfDeadlockAcquireResource(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViDeadlockExAcquireResourceExclusiveLite_Exit(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg4 = 0;
    if ((*(uint8_t *)(arg1 + 0x18)) != 0) {
        Arg2 = 8;
        Arg3 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = *(uint64_t *)(arg1);
        Arg4 = ((*(uint8_t *)(arg1 + 0x8)) == 0) ? 1 : 0;
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        v_stack_m18 = result;
        result = VfDeadlockAcquireResource(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA9440&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA9440[BB_00BA9440]
  bb_00BA944D[BB_00BA944D]
  bb_00BA9474[BB_00BA9474]
  bb_00BA9479[BB_00BA9479]
  bb_00BA9440 -->|branch| bb_00BA9474
  bb_00BA9440 -->|fallthrough| bb_00BA944D
  bb_00BA944D -->|flow| bb_00BA9474
```
