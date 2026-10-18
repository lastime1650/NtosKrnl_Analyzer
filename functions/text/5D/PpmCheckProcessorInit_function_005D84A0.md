# PpmCheckProcessorInit

- RVA: `0x005D84A0`–`0x005D84C8` (길이 `40` bytes)
- VA: `0x00000001405D84A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005D84B0` → [PpmResetPerfTimes](../44/PpmResetPerfTimes_function_0044F8EC.md) (function, `0x0044F8EC`)
- `0x005D84BA` → [PpmHeteroHgsProcessorInit](PpmHeteroHgsProcessorInit_function_005D8C08.md) (function, `0x005D8C08`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D84A0  40 53                           push rbx
005D84A2  48 83 EC 20                     sub rsp, 0x20
005D84A6  48 8B D9                        mov rbx, rcx
005D84A9  48 81 C1 B0 89 00 00            add rcx, 0x89b0
005D84B0  E8 37 74 E7 FF                  call 0x14044f8ec
005D84B5  33 D2                           xor edx, edx
005D84B7  48 8B CB                        mov rcx, rbx
005D84BA  E8 49 07 00 00                  call 0x1405d8c08
005D84BF  33 C0                           xor eax, eax
005D84C1  48 83 C4 20                     add rsp, 0x20
005D84C5  5B                              pop rbx
005D84C6  C3                              ret
005D84C7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmCheckProcessorInit(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (0x89B0ULL);
    result = PpmResetPerfTimes(a1, a2, a3, a4);
    a2 = 0;
    result = PpmHeteroHgsProcessorInit(a1, a2, a3, a4);
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmCheckProcessorInit(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (0x89B0ULL);
    result = PpmResetPerfTimes(Arg1, Arg2, a3, a4);
    Arg2 = 0;
    result = PpmHeteroHgsProcessorInit(Arg1, Arg2, a3, a4);
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D84A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D84A0[BB_005D84A0]
  bb_005D84C7[BB_005D84C7]
```
