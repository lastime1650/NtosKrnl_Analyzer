# MiStoreFreeWriteSupport

- RVA: `0x00203A48`–`0x00203A8B` (길이 `67` bytes)
- VA: `0x0000000140203A48`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `19`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00203A66` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x00203A7A` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)

### Direct callers
- [MiStoreModifiedWriteComplete](MiStoreModifiedWriteComplete_function_002045E8.md) at `0x00204618`
- [MiStoreWriteModifiedPages](../2B/MiStoreWriteModifiedPages_function_002B46C4.md) at `0x002B51DE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00203A48  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00203A4D  57                              push rdi
00203A4E  48 83 EC 20                     sub rsp, 0x20
00203A52  48 8B D9                        mov rbx, rcx
00203A55  48 8B FA                        mov rdi, rdx
00203A58  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00203A5C  48 85 C9                        test rcx, rcx
00203A5F  74 0F                           je 0x140203a70
00203A61  BA 4D 6D 50 66                  mov edx, 0x66506d4d
00203A66  E8 35 04 06 00                  call 0x140263ea0
00203A6B  48 83 63 18 00                  and qword ptr [rbx + 0x18], 0
00203A70  48 8D 8F 60 05 00 00            lea rcx, [rdi + 0x560]
00203A77  48 8B D3                        mov rdx, rbx
00203A7A  E8 31 6B 4B 00                  call 0x1406ba5b0
00203A7F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00203A84  48 83 C4 20                     add rsp, 0x20
00203A88  5F                              pop rdi
00203A89  C3                              ret
00203A8A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiStoreFreeWriteSupport(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 24) != 0) {
        a2 = 0x66506D4DULL;
        result = ObDereferenceObjectDeferDeleteWithTag(*(unsigned __int64 *)(a1 + 24), a2, a3, a4);
    }
    result = ExpInterlockedPushEntrySList(a2 + 1376, a1, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiStoreFreeWriteSupport(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x18) != 0) {
        Arg2 = 0x66506D4DULL;
        result = ObDereferenceObjectDeferDeleteWithTag(*(uint64_t *)(arg1 + 0x18), Arg2, a3, a4);
    }
    result = ExpInterlockedPushEntrySList(Arg2 + 1376, Arg1, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R/W` |
| `Arg2` | `+ 0x560` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00203A48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00203A48[BB_00203A48]
  bb_00203A61[BB_00203A61]
  bb_00203A70[BB_00203A70]
  bb_00203A8A[BB_00203A8A]
  bb_00203A48 -->|branch| bb_00203A70
  bb_00203A48 -->|fallthrough| bb_00203A61
  bb_00203A61 -->|flow| bb_00203A70
```
