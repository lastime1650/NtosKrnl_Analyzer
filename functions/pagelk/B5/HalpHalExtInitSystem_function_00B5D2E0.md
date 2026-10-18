# HalpHalExtInitSystem

- RVA: `0x00B5D2E0`–`0x00B5D2FB` (길이 `27` bytes)
- VA: `0x0000000140B5D2E0`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B5D2F0` → [HalpExtInitExtensions](../../init/C1/HalpExtInitExtensions_function_00C1F7FC.md) (function, `0x00C1F7FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B5D2F0` → [HalpExtInitExtensions](../../init/C1/HalpExtInitExtensions_function_00C1F7FC.md) (`PAGELK` → `INIT`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B5D2E0  48 83 EC 28                     sub rsp, 0x28
00B5D2E4  83 F9 08                        cmp ecx, 8
00B5D2E7  74 04                           je 0x140b5d2ed
00B5D2E9  33 C0                           xor eax, eax
00B5D2EB  EB 08                           jmp 0x140b5d2f5
00B5D2ED  49 8B C8                        mov rcx, r8
00B5D2F0  E8 07 25 0C 00                  call 0x140c1f7fc
00B5D2F5  48 83 C4 28                     add rsp, 0x28
00B5D2F9  C3                              ret
00B5D2FA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpHalExtInitSystem(int a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 == 8) goto loc_00B5D2ED;
    result = 0;
    goto loc_00B5D2F5;
loc_00B5D2ED:
    result = HalpExtInitExtensions(a3, a2, a3, a4);
loc_00B5D2F5:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpHalExtInitSystem(int32_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == 8) goto loc_00B5D2ED;
    result = 0;
    goto loc_00B5D2F5;
loc_00B5D2ED:
    result = HalpExtInitExtensions(Arg3, Arg2, Arg3, a4);
loc_00B5D2F5:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B5D2E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B5D2E0[BB_00B5D2E0]
  bb_00B5D2E9[BB_00B5D2E9]
  bb_00B5D2ED[BB_00B5D2ED]
  bb_00B5D2F5[BB_00B5D2F5]
  bb_00B5D2FA[BB_00B5D2FA]
  bb_00B5D2E0 -->|branch| bb_00B5D2ED
  bb_00B5D2E0 -->|fallthrough| bb_00B5D2E9
  bb_00B5D2E9 -->|branch| bb_00B5D2F5
  bb_00B5D2ED -->|flow| bb_00B5D2F5
```
