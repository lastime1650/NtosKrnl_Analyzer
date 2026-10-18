# EtwpCovSampModuleCleanup

- RVA: `0x0097D91C`–`0x0097D964` (길이 `72` bytes)
- VA: `0x000000014097D91C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `23`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0097D934` → [EtwpCovSampModuleNameInfoCleanup](EtwpCovSampModuleNameInfoCleanup_function_0097D96C.md) (function, `0x0097D96C`)
- `0x0097D94C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [EtwpCovSampContextGetModule](../8D/EtwpCovSampContextGetModule_function_008D7FEC.md) at `0x008D8E6F`
- [EtwpCovSampContextPruneModules](../8D/EtwpCovSampContextPruneModules_function_008DA03C.md) at `0x008DA510`
- [EtwpCovSampContextRemoveAndFreeModule](EtwpCovSampContextRemoveAndFreeModule_function_0097D870.md) at `0x0097D8EF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0097D94C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0097D91C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0097D921  57                              push rdi
0097D922  48 83 EC 20                     sub rsp, 0x20
0097D926  48 8B D9                        mov rbx, rcx
0097D929  33 FF                           xor edi, edi
0097D92B  48 83 C1 68                     add rcx, 0x68
0097D92F  48 39 39                        cmp qword ptr [rcx], rdi
0097D932  74 0D                           je 0x14097d941
0097D934  E8 33 00 00 00                  call 0x14097d96c
0097D939  48 89 7B 70                     mov qword ptr [rbx + 0x70], rdi
0097D93D  66 89 7B 78                     mov word ptr [rbx + 0x78], di
0097D941  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
0097D945  48 85 C9                        test rcx, rcx
0097D948  74 0E                           je 0x14097d958
0097D94A  33 D2                           xor edx, edx
0097D94C  E8 1F 4F 20 00                  call 0x140b82870
0097D951  48 89 7B 30                     mov qword ptr [rbx + 0x30], rdi
0097D955  89 7B 38                        mov dword ptr [rbx + 0x38], edi
0097D958  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0097D95D  48 83 C4 20                     add rsp, 0x20
0097D961  5F                              pop rdi
0097D962  C3                              ret
0097D963  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCovSampModuleCleanup(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
    a1 = (a1) + (104);
    if ((*(unsigned __int64 *)(a1)) != 0) {
        result = EtwpCovSampModuleNameInfoCleanup(a1, a2, a3, a4);
        *(unsigned __int64 *)(a1 + 112) = 0;
        *(unsigned __int16 *)(a1 + 120) = 0;
    }
    if (*(unsigned __int64 *)(a1 + 48) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 48), a2, a3, a4);
        *(unsigned __int64 *)(a1 + 48) = 0;
        *(unsigned int *)(a1 + 56) = 0;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCovSampModuleCleanup(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    Arg1 = (Arg1) + (104);
    if ((*(uint64_t *)(arg1)) != 0) {
        result = EtwpCovSampModuleNameInfoCleanup(Arg1, Arg2, a3, a4);
        *(uint64_t *)(arg1 + 0x70) = 0;
        *(uint16_t *)(arg1 + 0x78) = 0;
    }
    if (*(uint64_t *)(arg1 + 0x30) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x30), Arg2, a3, a4);
        *(uint64_t *)(arg1 + 0x30) = 0;
        *(uint32_t *)(arg1 + 0x38) = 0;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x70` | `64` | `W` |
| `Arg1` | `+ 0x78` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097D91C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0097D91C[BB_0097D91C]
  bb_0097D934[BB_0097D934]
  bb_0097D941[BB_0097D941]
  bb_0097D94A[BB_0097D94A]
  bb_0097D958[BB_0097D958]
  bb_0097D963[BB_0097D963]
  bb_0097D91C -->|branch| bb_0097D941
  bb_0097D91C -->|fallthrough| bb_0097D934
  bb_0097D934 -->|flow| bb_0097D941
  bb_0097D941 -->|branch| bb_0097D958
  bb_0097D941 -->|fallthrough| bb_0097D94A
  bb_0097D94A -->|flow| bb_0097D958
```
