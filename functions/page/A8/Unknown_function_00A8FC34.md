# sub_00A8FC34

- RVA: `0x00A8FC34`–`0x00A8FC5E` (길이 `42` bytes)
- VA: `0x0000000140A8FC34`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000805BC`
- 디코드: `14`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A8FC45` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)

### Direct callers
- [sub_008D4104](../8D/Unknown_function_008D4104.md) at `0x008D4135`
- [sub_008D4104](../8D/Unknown_function_008D4104.md) at `0x008D4162`
- [sub_008D4104](../8D/Unknown_function_008D4104.md) at `0x008D41CC`
- [sub_008D4104](../8D/Unknown_function_008D4104.md) at `0x008D41FF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8FC34  48 85 C9                        test rcx, rcx
00A8FC37  74 23                           je 0x140a8fc5c
00A8FC39  53                              push rbx
00A8FC3A  48 83 EC 20                     sub rsp, 0x20
00A8FC3E  48 8B D9                        mov rbx, rcx
00A8FC41  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00A8FC45  E8 BA 27 E4 FF                  call 0x1408d2404
00A8FC4A  48 83 63 10 00                  and qword ptr [rbx + 0x10], 0
00A8FC4F  83 63 04 00                     and dword ptr [rbx + 4], 0
00A8FC53  83 63 08 00                     and dword ptr [rbx + 8], 0
00A8FC57  48 83 C4 20                     add rsp, 0x20
00A8FC5B  5B                              pop rbx
00A8FC5C  C3                              ret
00A8FC5D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00A8FC34(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    if (a1 != 0) {
        v_rsp = (v_rsp) - (32);
        v_rbx = a1;
        a1 = *(unsigned __int64 *)(a1 + 16);
        result = PdcCloseEvent(a1, a2, a3, a4);
        v_rsp = (v_rsp) + (32);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00A8FC34(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    if (Arg1 != 0) {
        local_rsp = (local_rsp) - (32);
        local_rbx = Arg1;
        Arg1 = *(uint64_t *)(Arg1 + 0x10);
        result = PdcCloseEvent(Arg1, a2, a3, a4);
        local_rsp = (local_rsp) + (32);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8FC34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8FC34[BB_00A8FC34]
  bb_00A8FC39[BB_00A8FC39]
  bb_00A8FC5C[BB_00A8FC5C]
  bb_00A8FC5D[BB_00A8FC5D]
  bb_00A8FC34 -->|branch| bb_00A8FC5C
  bb_00A8FC34 -->|fallthrough| bb_00A8FC39
  bb_00A8FC39 -->|flow| bb_00A8FC5C
```
