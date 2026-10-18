# PoDeviceAcquireIrp

- RVA: `0x0038FF88`–`0x0038FFBC` (길이 `52` bytes)
- VA: `0x000000014038FF88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `15`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0038FFB1` → [PopDiagTraceDeviceAcquireIrp](../39/PopDiagTraceDeviceAcquireIrp_function_00390498.md) (function, `0x00390498`)

### Direct callers
- [PopIrpWorker](../26/PopIrpWorker_function_0026D410.md) at `0x0026D5A1`
- [IopfCompleteRequest](../29/IopfCompleteRequest_function_0029B5F8.md) at `0x0029B781`
- [PoHandleIrp](../47/PoHandleIrp_function_004709D0.md) at `0x00470B0C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0038FF88  48 83 EC 28                     sub rsp, 0x28
0038FF8C  80 EA 02                        sub dl, 2
0038FF8F  80 FA 01                        cmp dl, 1
0038FF92  77 22                           ja 0x14038ffb6
0038FF94  4D 85 C0                        test r8, r8
0038FF97  74 1D                           je 0x14038ffb6
0038FF99  48 0F BE 41 42                  movsx rax, byte ptr [rcx + 0x42]
0038FF9E  48 8D 14 C0                     lea rdx, [rax + rax*8]
0038FFA2  48 8B 84 D1 C8 00 00 00         mov rax, qword ptr [rcx + rdx*8 + 0xc8]
0038FFAA  49 8B D0                        mov rdx, r8
0038FFAD  4C 89 40 28                     mov qword ptr [rax + 0x28], r8
0038FFB1  E8 E2 04 00 00                  call 0x140390498
0038FFB6  48 83 C4 28                     add rsp, 0x28
0038FFBA  C3                              ret
0038FFBB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoDeviceAcquireIrp(__int64 a1, unsigned __int8 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = (unsigned __int8)((a2) - (2));
    if (a2 > 1) goto loc_0038FFB6;
    if (a3 != 0) {
        result = (__int8)(*(unsigned __int8 *)(a1 + 66));
        a2 = result + result * 8;
        result = *(unsigned __int64 *)(a1 + a2 * 8 + 200);
        a2 = a3;
        *(unsigned __int64 *)(result + 40) = a3;
        result = PopDiagTraceDeviceAcquireIrp(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PoDeviceAcquireIrp(void *Arg1, uint8_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = (uint8_t)((Arg2) - (2));
    if (Arg2 > 1) goto loc_0038FFB6;
    if (Arg3 != 0) {
        result = (int8_t)(*(uint8_t *)(arg1 + 0x42));
        Arg2 = result + result * 8;
        result = *(uint64_t *)(arg1 + Arg2 * 8 + 0xC8);
        Arg2 = Arg3;
        *(uint64_t *)(result + 0x28) = Arg3;
        result = PopDiagTraceDeviceAcquireIrp(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x42` | `8` | `R` |
| `Arg1` | `+ 0xC8 + rdx*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038FF88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0038FF88[BB_0038FF88]
  bb_0038FF94[BB_0038FF94]
  bb_0038FF99[BB_0038FF99]
  bb_0038FFB6[BB_0038FFB6]
  bb_0038FFBB[BB_0038FFBB]
  bb_0038FF88 -->|branch| bb_0038FFB6
  bb_0038FF88 -->|fallthrough| bb_0038FF94
  bb_0038FF94 -->|branch| bb_0038FFB6
  bb_0038FF94 -->|fallthrough| bb_0038FF99
  bb_0038FF99 -->|flow| bb_0038FFB6
```
