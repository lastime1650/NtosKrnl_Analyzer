# PspQueryProcessDefaultQos

- RVA: `0x005E30E0`–`0x005E30F7` (길이 `23` bytes)
- VA: `0x00000001405E30E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005E30E7` → [KeCalculateProcessDefaultQos](../5C/KeCalculateProcessDefaultQos_function_005CA5A0.md) (function, `0x005CA5A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E30E0  48 83 EC 28                     sub rsp, 0x28
005E30E4  4C 8B CA                        mov r9, rdx
005E30E7  E8 B4 74 FE FF                  call 0x1405ca5a0
005E30EC  41 88 01                        mov byte ptr [r9], al
005E30EF  33 C0                           xor eax, eax
005E30F1  48 83 C4 28                     add rsp, 0x28
005E30F5  C3                              ret
005E30F6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspQueryProcessDefaultQos(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = KeCalculateProcessDefaultQos(a1, a2, a3, a2);
    *(unsigned __int8 *)(a2) = (unsigned __int8)(result);
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspQueryProcessDefaultQos(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = KeCalculateProcessDefaultQos(Arg1, Arg2, a3, Arg2);
    *(uint8_t *)(Arg2) = (uint8_t)(result);
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E30E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E30E0[BB_005E30E0]
  bb_005E30F6[BB_005E30F6]
```
