# KeUpdateTebSchedulingPropertiesCurrentThread

- RVA: `0x003C48E8`–`0x003C490D` (길이 `37` bytes)
- VA: `0x00000001403C48E8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003C48FD` → [KiUpdateTebSchedulingPropertiesCurrentThread](KiUpdateTebSchedulingPropertiesCurrentThread_function_003C4938.md) (function, `0x003C4938`)
- `0x003C4902` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [PspUserThreadStartup](../../page/8D/PspUserThreadStartup_function_008D5B10.md) at `0x008D5BA4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C48E8  48 83 EC 28                     sub rsp, 0x28
003C48EC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003C48F5  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
003C48FC  90                              nop
003C48FD  E8 36 00 00 00                  call 0x1403c4938
003C4902  E8 A9 8F E9 FF                  call 0x14025d8b0
003C4907  48 83 C4 28                     add rsp, 0x28
003C490B  C3                              ret
003C490C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeUpdateTebSchedulingPropertiesCurrentThread(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = KiUpdateTebSchedulingPropertiesCurrentThread(a1, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void KeUpdateTebSchedulingPropertiesCurrentThread(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = KiUpdateTebSchedulingPropertiesCurrentThread(a1, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C48E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003C48E8[BB_003C48E8]
  bb_003C490C[BB_003C490C]
```
