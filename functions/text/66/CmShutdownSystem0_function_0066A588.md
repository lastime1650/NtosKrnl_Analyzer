# CmShutdownSystem0

- RVA: `0x0066A588`–`0x0066A5A7` (길이 `31` bytes)
- VA: `0x000000014066A588`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0066A58E` → [CmFcShutdownSystem](../../page/7E/CmFcShutdownSystem_function_007E5BC4.md) (function, `0x007E5BC4`)

### Direct callers
- [CmShutdownSystem](../../page/7E/CmShutdownSystem_function_007E5174.md) at `0x007E51B3`

### Static image references
- `0x0066A593` → RVA `0x00EEFC20` (`.data`; read/write)
- `0x0066A59A` → RVA `0x00EEFC3D` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0066A58E` → [CmFcShutdownSystem](../../page/7E/CmFcShutdownSystem_function_007E5BC4.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066A588  48 83 EC 28                     sub rsp, 0x28
0066A58C  33 C9                           xor ecx, ecx
0066A58E  E8 31 B6 17 00                  call 0x1407e5bc4
0066A593  83 25 86 56 88 00 00            and dword ptr [rip + 0x885686], 0
0066A59A  C6 05 9C 56 88 00 01            mov byte ptr [rip + 0x88569c], 1
0066A5A1  48 83 C4 28                     add rsp, 0x28
0066A5A5  C3                              ret
0066A5A6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmShutdownSystem0(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = 0;
    result = CmFcShutdownSystem(a1, a2, a3, a4);
    *(unsigned __int8 *)(v_rip + 8935068) = 1;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmShutdownSystem0(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = 0;
    result = CmFcShutdownSystem(Arg1, a2, a3, a4);
    *(uint8_t *)(v_rip + 0x88569C) = 1;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066A588&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066A588[BB_0066A588]
  bb_0066A5A6[BB_0066A5A6]
```
