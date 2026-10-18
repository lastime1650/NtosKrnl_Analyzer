# RtlpValidateContextFlags

- RVA: `0x0049BF20`–`0x0049BF39` (길이 `25` bytes)
- VA: `0x000000014049BF20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0049BF2E` → [RtlpValidateContextFlags2](../4E/RtlpValidateContextFlags2_function_004EF138.md) (function, `0x004EF138`)

### Direct callers
- [RtlpWow64SanitizeContextFlags](../../page/8C/RtlpWow64SanitizeContextFlags_function_008CDF00.md) at `0x008CDF25`
- [RtlpWriteExtendedContext](../../page/8D/RtlpWriteExtendedContext_function_008D4A5C.md) at `0x008D4A8C`
- [RtlCopyContext](../../page/8D/RtlCopyContext_function_008D5940.md) at `0x008D5976`
- [RtlCopyContext](../../page/8D/RtlCopyContext_function_008D5940.md) at `0x008D59AD`
- [RtlCopyContext](../../page/8D/RtlCopyContext_function_008D5940.md) at `0x008D59C0`
- [RtlCopyContext](../../page/8D/RtlCopyContext_function_008D5940.md) at `0x008D59D4`
- [RtlpReadExtendedContext](../../page/8D/RtlpReadExtendedContext_function_008D61D0.md) at `0x008D6243`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049BF20  48 83 EC 28                     sub rsp, 0x28
0049BF24  49 B8 D8 03 00 00 80 F7 FF FF   movabs r8, 0xfffff780000003d8
0049BF2E  E8 05 32 05 00                  call 0x1404ef138
0049BF33  48 83 C4 28                     add rsp, 0x28
0049BF37  C3                              ret
0049BF38  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpValidateContextFlags(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RtlpValidateContextFlags2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void RtlpValidateContextFlags(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RtlpValidateContextFlags2(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049BF20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049BF20[BB_0049BF20]
  bb_0049BF38[BB_0049BF38]
```
