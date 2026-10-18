# KeAndAffinityEx

- RVA: `0x004FC0E0`–`0x004FC101` (길이 `33` bytes)
- VA: `0x00000001404FC0E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FC0E9` → [KiAndAffinityExNoResult](../2C/KiAndAffinityExNoResult_function_002CF84C.md) (function, `0x002CF84C`)
- `0x004FC0F6` → [KiAndAffinityEx](../3C/KiAndAffinityEx_function_003C0680.md) (function, `0x003C0680`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FC0E0  48 83 EC 28                     sub rsp, 0x28
004FC0E4  4D 85 C0                        test r8, r8
004FC0E7  75 07                           jne 0x1404fc0f0
004FC0E9  E8 5E 37 DD FF                  call 0x1402cf84c
004FC0EE  EB 0B                           jmp 0x1404fc0fb
004FC0F0  41 B9 14 00 00 00               mov r9d, 0x14
004FC0F6  E8 85 45 EC FF                  call 0x1403c0680
004FC0FB  48 83 C4 28                     add rsp, 0x28
004FC0FF  C3                              ret
004FC100  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeAndAffinityEx(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 != 0) goto loc_004FC0F0;
    result = KiAndAffinityExNoResult(a1, a2, a3, a4);
    goto loc_004FC0FB;
loc_004FC0F0:
    result = KiAndAffinityEx(a1, a2, a3, 20);
loc_004FC0FB:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeAndAffinityEx(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 != 0) goto loc_004FC0F0;
    result = KiAndAffinityExNoResult(Arg1, Arg2, Arg3, a4);
    goto loc_004FC0FB;
loc_004FC0F0:
    result = KiAndAffinityEx(Arg1, Arg2, Arg3, 20);
loc_004FC0FB:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FC0E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FC0E0[BB_004FC0E0]
  bb_004FC0E9[BB_004FC0E9]
  bb_004FC0F0[BB_004FC0F0]
  bb_004FC0FB[BB_004FC0FB]
  bb_004FC100[BB_004FC100]
  bb_004FC0E0 -->|branch| bb_004FC0F0
  bb_004FC0E0 -->|fallthrough| bb_004FC0E9
  bb_004FC0E9 -->|branch| bb_004FC0FB
  bb_004FC0F0 -->|flow| bb_004FC0FB
```
