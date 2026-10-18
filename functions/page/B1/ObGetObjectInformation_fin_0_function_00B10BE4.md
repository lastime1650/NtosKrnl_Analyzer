# ObGetObjectInformation$fin$0

- RVA: `0x00B10BE4`–`0x00B10C1E` (길이 `58` bytes)
- VA: `0x0000000140B10BE4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A3420`
- 디코드: `18`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B10BF6` → [ObpDestroyTypeArray](../9D/ObpDestroyTypeArray_function_009DB464.md) (function, `0x009DB464`)
- `0x00B10C00` → [ObpDestroyTypeArray](../9D/ObpDestroyTypeArray_function_009DB464.md) (function, `0x009DB464`)
- `0x00B10C11` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B10C11` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B10BE4  40 55                           push rbp
00B10BE6  48 83 EC 30                     sub rsp, 0x30
00B10BEA  48 8B EA                        mov rbp, rdx
00B10BED  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
00B10BF1  48 85 C9                        test rcx, rcx
00B10BF4  74 06                           je 0x140b10bfc
00B10BF6  E8 69 A8 EC FF                  call 0x1409db464
00B10BFB  90                              nop
00B10BFC  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
00B10C00  E8 5F A8 EC FF                  call 0x1409db464
00B10C05  BA 4F 62 41 72                  mov edx, 0x7241624f
00B10C0A  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
00B10C11  E8 5A 1C 07 00                  call 0x140b82870
00B10C16  90                              nop
00B10C17  48 83 C4 30                     add rsp, 0x30
00B10C1B  5D                              pop rbp
00B10C1C  C3                              ret
00B10C1D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObGetObjectInformation_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    if (*(unsigned __int64 *)(a2 + 112) != 0) {
        result = ObpDestroyTypeArray(*(unsigned __int64 *)(a2 + 112), a2, a3, a4);
    }
    result = ObpDestroyTypeArray(*(unsigned __int64 *)(a2 + 120), a2, a3, a4);
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a2 + 128), (unsigned int)(0x7241624FULL), a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObGetObjectInformation_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    if (*(uint64_t *)(arg2 + 0x70) != 0) {
        result = ObpDestroyTypeArray(*(uint64_t *)(arg2 + 0x70), Arg2, a3, a4);
    }
    result = ObpDestroyTypeArray(*(uint64_t *)(arg2 + 0x78), Arg2, a3, a4);
    result = ExFreePoolWithTag(*(uint64_t *)(arg2 + 0x80), (uint32_t)(0x7241624FULL), a3, a4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x70` | `64` | `R` |
| `Arg2` | `+ 0x78` | `64` | `R` |
| `Arg2` | `+ 0x80` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B10BE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B10BE4[BB_00B10BE4]
  bb_00B10BF6[BB_00B10BF6]
  bb_00B10BFC[BB_00B10BFC]
  bb_00B10C1D[BB_00B10C1D]
  bb_00B10BE4 -->|branch| bb_00B10BFC
  bb_00B10BE4 -->|fallthrough| bb_00B10BF6
  bb_00B10BF6 -->|flow| bb_00B10BFC
```
