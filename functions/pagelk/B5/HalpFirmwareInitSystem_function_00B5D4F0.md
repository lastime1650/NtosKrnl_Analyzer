# HalpFirmwareInitSystem

- RVA: `0x00B5D4F0`–`0x00B5D509` (길이 `25` bytes)
- VA: `0x0000000140B5D4F0`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B5D4FC` → [HalpFirmwareInitDiscard](../../init/C1/HalpFirmwareInitDiscard_function_00C1FCE0.md) (function, `0x00C1FCE0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B5D4FC` → [HalpFirmwareInitDiscard](../../init/C1/HalpFirmwareInitDiscard_function_00C1FCE0.md) (`PAGELK` → `INIT`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B5D4F0  48 83 EC 28                     sub rsp, 0x28
00B5D4F4  83 F9 07                        cmp ecx, 7
00B5D4F7  75 08                           jne 0x140b5d501
00B5D4F9  49 8B C8                        mov rcx, r8
00B5D4FC  E8 DF 27 0C 00                  call 0x140c1fce0
00B5D501  33 C0                           xor eax, eax
00B5D503  48 83 C4 28                     add rsp, 0x28
00B5D507  C3                              ret
00B5D508  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpFirmwareInitSystem(int a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 == 7) {
        a1 = a3;
        result = HalpFirmwareInitDiscard(a1, a2, a3, a4);
    }
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpFirmwareInitSystem(int32_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == 7) {
        Arg1 = Arg3;
        result = HalpFirmwareInitDiscard(Arg1, Arg2, Arg3, a4);
    }
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B5D4F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B5D4F0[BB_00B5D4F0]
  bb_00B5D4F9[BB_00B5D4F9]
  bb_00B5D501[BB_00B5D501]
  bb_00B5D508[BB_00B5D508]
  bb_00B5D4F0 -->|branch| bb_00B5D501
  bb_00B5D4F0 -->|fallthrough| bb_00B5D4F9
  bb_00B5D4F9 -->|flow| bb_00B5D501
```
