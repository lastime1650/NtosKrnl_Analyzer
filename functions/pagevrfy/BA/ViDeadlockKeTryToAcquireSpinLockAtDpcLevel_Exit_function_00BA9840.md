# ViDeadlockKeTryToAcquireSpinLockAtDpcLevel_Exit

- RVA: `0x00BA9840`–`0x00BA9873` (길이 `51` bytes)
- VA: `0x0000000140BA9840`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `13`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA9868` → [VfDeadlockAcquireResource](../BB/VfDeadlockAcquireResource_function_00BB83B4.md) (function, `0x00BB83B4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA9840  48 83 EC 38                     sub rsp, 0x38
00BA9844  80 79 10 00                     cmp byte ptr [rcx + 0x10], 0
00BA9848  74 23                           je 0x140ba986d
00BA984A  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
00BA9853  BA 05 00 00 00                  mov edx, 5
00BA9858  48 8B 01                        mov rax, qword ptr [rcx]
00BA985B  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00BA985F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BA9864  44 8D 4A FC                     lea r9d, [rdx - 4]
00BA9868  E8 47 EB 00 00                  call 0x140bb83b4
00BA986D  48 83 C4 38                     add rsp, 0x38
00BA9871  C3                              ret
00BA9872  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViDeadlockKeTryToAcquireSpinLockAtDpcLevel_Exit(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    if ((*(unsigned __int8 *)(a1 + 16)) != 0) {
        a3 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = 5;
        result = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 8);
        v_stack_m18 = result;
        a4 = a2 - 4;
        result = VfDeadlockAcquireResource(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViDeadlockKeTryToAcquireSpinLockAtDpcLevel_Exit(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    if ((*(uint8_t *)(arg1 + 0x10)) != 0) {
        a3 = *(uint64_t *)(gs_base + (0 + 0x188));
        a2 = 5;
        result = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        v_stack_m18 = result;
        a4 = a2 - 4;
        result = VfDeadlockAcquireResource(Arg1, a2, a3, a4);
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
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA9840&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA9840[BB_00BA9840]
  bb_00BA984A[BB_00BA984A]
  bb_00BA986D[BB_00BA986D]
  bb_00BA9872[BB_00BA9872]
  bb_00BA9840 -->|branch| bb_00BA986D
  bb_00BA9840 -->|fallthrough| bb_00BA984A
  bb_00BA984A -->|flow| bb_00BA986D
```
