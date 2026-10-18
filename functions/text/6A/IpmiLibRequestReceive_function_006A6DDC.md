# IpmiLibRequestReceive

- RVA: `0x006A6DDC`–`0x006A6DFB` (길이 `31` bytes)
- VA: `0x00000001406A6DDC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006A6DF0` → [IpmiLibpKcsRequestAndReceive](IpmiLibpKcsRequestAndReceive_function_006A7210.md) (function, `0x006A7210`)

### Direct callers
- [IpmiLibAddSelRecord](IpmiLibAddSelRecord_function_006A6C78.md) at `0x006A6CC7`

### Static image references
- `0x006A6DE0` → RVA `0x00EFA084` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A6DDC  48 83 EC 28                     sub rsp, 0x28
006A6DE0  83 3D 9D 32 85 00 01            cmp dword ptr [rip + 0x85329d], 1
006A6DE7  74 07                           je 0x1406a6df0
006A6DE9  B8 BB 00 00 C0                  mov eax, 0xc00000bb
006A6DEE  EB 05                           jmp 0x1406a6df5
006A6DF0  E8 1B 04 00 00                  call 0x1406a7210
006A6DF5  48 83 C4 28                     add rsp, 0x28
006A6DF9  C3                              ret
006A6DFA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IpmiLibRequestReceive(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 8729245)) == 1) goto loc_006A6DF0;
    goto loc_006A6DF5;
loc_006A6DF0:
    result = IpmiLibpKcsRequestAndReceive(a1, a2, a3, a4);
loc_006A6DF5:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void IpmiLibRequestReceive(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0x85329D)) == 1) goto loc_006A6DF0;
    goto loc_006A6DF5;
loc_006A6DF0:
    result = IpmiLibpKcsRequestAndReceive(a1, a2, a3, a4);
loc_006A6DF5:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A6DDC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006A6DDC[BB_006A6DDC]
  bb_006A6DE9[BB_006A6DE9]
  bb_006A6DF0[BB_006A6DF0]
  bb_006A6DF5[BB_006A6DF5]
  bb_006A6DFA[BB_006A6DFA]
  bb_006A6DDC -->|branch| bb_006A6DF0
  bb_006A6DDC -->|fallthrough| bb_006A6DE9
  bb_006A6DE9 -->|branch| bb_006A6DF5
  bb_006A6DF0 -->|flow| bb_006A6DF5
```
