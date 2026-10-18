# MmReturnPoolQuota

- RVA: `0x00390EE0`–`0x00390EF7` (길이 `23` bytes)
- VA: `0x0000000140390EE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PspReturnResourceQuota](../38/PspReturnResourceQuota_function_0038FFC4.md) at `0x0039001C`
- [PspReturnQuota](PspReturnQuota_function_00390C40.md) at `0x00390DB4`

### Static image references
- `0x00390EE5` → RVA `0x00E2CBD8` (`.data`; read/write)
- `0x00390EEE` → RVA `0x00E2CBD0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00390EE0  83 F9 01                        cmp ecx, 1
00390EE3  74 09                           je 0x140390eee
00390EE5  48 29 15 EC BC A9 00            sub qword ptr [rip + 0xa9bcec], rdx
00390EEC  C3                              ret
00390EED  CC                              int3
00390EEE  48 29 15 DB BC A9 00            sub qword ptr [rip + 0xa9bcdb], rdx
00390EF5  C3                              ret
00390EF6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MmReturnPoolQuota(int a1, __int64 a2)
{
    if (a1 == 1) goto loc_00390EEE;
    return;
loc_00390EEE:
    return;
}
```

## 5. (Beta) C Style

```c
void MmReturnPoolQuota(int32_t Arg1, int64_t Arg2)
{
    if (Arg1 == 1) goto loc_00390EEE;
    return;
loc_00390EEE:
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00390EE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00390EE0[BB_00390EE0]
  bb_00390EE5[BB_00390EE5]
  bb_00390EED[BB_00390EED]
  bb_00390EEE[BB_00390EEE]
  bb_00390EF6[BB_00390EF6]
  bb_00390EE0 -->|branch| bb_00390EEE
  bb_00390EE0 -->|fallthrough| bb_00390EE5
  bb_00390EED -->|flow| bb_00390EEE
```
