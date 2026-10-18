# FsRtlAllocatePool

- RVA: `0x00581BD0`–`0x00581BF7` (길이 `39` bytes)
- VA: `0x0000000140581BD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00581BDC` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x00581BEB` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00581BDC` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00581BD0  48 83 EC 28                     sub rsp, 0x28
00581BD4  8B D2                           mov edx, edx
00581BD6  41 B8 46 53 72 74               mov r8d, 0x74725346
00581BDC  E8 2F 04 60 00                  call 0x140b82010
00581BE1  48 85 C0                        test rax, rax
00581BE4  75 0B                           jne 0x140581bf1
00581BE6  B9 9A 00 00 C0                  mov ecx, 0xc000009a
00581BEB  E8 60 4E D7 FF                  call 0x1402f6a50
00581BF0  CC                              int3
00581BF1  48 83 C4 28                     add rsp, 0x28
00581BF5  C3                              ret
00581BF6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlAllocatePool(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAllocatePoolWithTag(a1, (unsigned int)(a2), (unsigned int)(0x74725346ULL), a4);
    if (result == 0) {
        a1 = 0xC000009AULL;
        result = RtlRaiseStatus(a1, (unsigned int)(a2), (unsigned int)(0x74725346ULL), a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlAllocatePool(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAllocatePoolWithTag(Arg1, (uint32_t)(Arg2), (uint32_t)(0x74725346ULL), a4);
    if (result == 0) {
        Arg1 = 0xC000009AULL;
        result = RtlRaiseStatus(Arg1, (uint32_t)(Arg2), (uint32_t)(0x74725346ULL), a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00581BD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00581BD0[BB_00581BD0]
  bb_00581BE6[BB_00581BE6]
  bb_00581BF1[BB_00581BF1]
  bb_00581BF6[BB_00581BF6]
  bb_00581BD0 -->|branch| bb_00581BF1
  bb_00581BD0 -->|fallthrough| bb_00581BE6
  bb_00581BE6 -->|flow| bb_00581BF1
```
