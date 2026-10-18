# ObpIncrPointerCount

- RVA: `0x00430BB0`–`0x00430BE5` (길이 `53` bytes)
- VA: `0x0000000140430BB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076F28`
- 디코드: `16`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00430BDF` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [PopPushPowerStateTransitionRecordWithCallback](PopPushPowerStateTransitionRecordWithCallback_function_00430A04.md) at `0x00430A8B`
- [PopPushPowerStateTransitionRecordWithCallback](PopPushPowerStateTransitionRecordWithCallback_function_00430A04.md) at `0x00430AA6`
- [ObpReferenceProcessObjectByHandle](../../page/89/ObpReferenceProcessObjectByHandle_function_00893C00.md) at `0x00893DB0`
- [ObpReferenceProcessObjectByHandle](../../page/89/ObpReferenceProcessObjectByHandle_function_00893C00.md) at `0x00893E37`
- [ObDuplicateObject](../../page/8C/ObDuplicateObject_function_008C4FA0.md) at `0x008C5887`
- [ObDuplicateObject](../../page/8C/ObDuplicateObject_function_008C4FA0.md) at `0x008C5B37`
- [ObInheritObjectHandle](../../page/94/ObInheritObjectHandle_function_0094D1C4.md) at `0x0094D1FA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00430BB0  48 83 EC 38                     sub rsp, 0x38
00430BB4  B8 01 00 00 00                  mov eax, 1
00430BB9  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
00430BBE  48 FF C0                        inc rax
00430BC1  48 83 F8 01                     cmp rax, 1
00430BC5  7E 06                           jle 0x140430bcd
00430BC7  48 83 C4 38                     add rsp, 0x38
00430BCB  C3                              ret
00430BCC  CC                              int3
00430BCD  33 D2                           xor edx, edx
00430BCF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00430BD4  4C 8D 41 30                     lea r8, [rcx + 0x30]
00430BD8  44 8D 4A 10                     lea r9d, [rdx + 0x10]
00430BDC  8D 4A 18                        lea ecx, [rdx + 0x18]
00430BDF  E8 7C CA 0C 00                  call 0x1404fd660
00430BE4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpIncrPointerCount(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (56);
    result = (1) + 1;
    if (result <= 1) goto loc_00430BCD;
    v_rsp = (v_rsp) + (56);
    return result;
loc_00430BCD:
    a2 = 0;
    v_stack_p20 = result;
    result = KeBugCheckEx(a2 + 24, a2, a1 + 48, a2 + 16);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObpIncrPointerCount(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (56);
    result = (1) + 1;
    if (result <= 1) goto loc_00430BCD;
    local_rsp = (local_rsp) + (56);
    return result;
loc_00430BCD:
    Arg2 = 0;
    v_stack_p20 = result;
    result = KeBugCheckEx(Arg2 + 24, Arg2, Arg1 + 48, Arg2 + 16);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00430BB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00430BB0[BB_00430BB0]
  bb_00430BC7[BB_00430BC7]
  bb_00430BCC[BB_00430BCC]
  bb_00430BCD[BB_00430BCD]
  bb_00430BB0 -->|branch| bb_00430BCD
  bb_00430BB0 -->|fallthrough| bb_00430BC7
  bb_00430BCC -->|flow| bb_00430BCD
```
