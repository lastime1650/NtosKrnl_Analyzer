# RtlFindClearBitsEx

- RVA: `0x003FAF30`–`0x003FAF5D` (길이 `45` bytes)
- VA: `0x00000001403FAF30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00098540`
- 디코드: `16`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiFindEmptyAddressRange](../../page/88/MiFindEmptyAddressRange_function_00886050.md) at `0x008861AE`
- [MiSelectImageBase](../../page/98/MiSelectImageBase_function_009887B0.md) at `0x0098893D`
- [MiSelectRelocationStartHint](../../page/A4/MiSelectRelocationStartHint_function_00A448A8.md) at `0x00A448E2`
- [sub_00B2B51A](../../page/B2/Unknown_function_00B2B51A.md) at `0x00B2B612`
- [sub_00B3ADEC](../../page/B3/Unknown_function_00B3ADEC.md) at `0x00B3AE67`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003FAF50` → [sub_003FAF5D](Unknown_function_003FAF5D.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003FAF30  40 57                           push rdi
003FAF32  48 83 EC 20                     sub rsp, 0x20
003FAF36  4C 8B 09                        mov r9, qword ptr [rcx]
003FAF39  33 C0                           xor eax, eax
003FAF3B  48 8B 79 08                     mov rdi, qword ptr [rcx + 8]
003FAF3F  4D 3B C1                        cmp r8, r9
003FAF42  4C 8B D2                        mov r10, rdx
003FAF45  49 0F 42 C0                     cmovb rax, r8
003FAF49  49 8D 51 FF                     lea rdx, [r9 - 1]
003FAF4D  4D 85 D2                        test r10, r10
003FAF50  75 0B                           jne 0x1403faf5d
003FAF52  48 83 E0 F8                     and rax, 0xfffffffffffffff8
003FAF56  48 83 C4 20                     add rsp, 0x20
003FAF5A  5F                              pop rdi
003FAF5B  C3                              ret
003FAF5C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlFindClearBitsEx(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = 0;
    if (a3 < (*(unsigned __int64 *)(a1))) { result = a3; }
    result = (result) & (-8);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlFindClearBitsEx(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = 0;
    if (Arg3 < (*(uint64_t *)(arg1))) { result = Arg3; }
    result = (result) & (-8);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FAF30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FAF30[BB_003FAF30]
  bb_003FAF52[BB_003FAF52]
  bb_003FAF5C[BB_003FAF5C]
  bb_003FAF30 -->|fallthrough| bb_003FAF52
```
