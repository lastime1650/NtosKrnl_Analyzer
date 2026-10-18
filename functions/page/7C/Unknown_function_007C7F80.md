# sub_007C7F80

- RVA: `0x007C7F80`–`0x007C7FAA` (길이 `42` bytes)
- VA: `0x00000001407C7F80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `12`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007C7F9F` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)

### Direct callers
- [sub_007C87A4](Unknown_function_007C87A4.md) at `0x007C8A37`
- [SLUpdateLicenseDataInternal](SLUpdateLicenseDataInternal_function_007C9C04.md) at `0x007CA8B9`
- [sub_009669C4](../96/Unknown_function_009669C4.md) at `0x00966BF9`

### Static image references
- `0x007C7F87` → RVA `0x00EFFA28` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007C7F9F` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C7F80  48 83 EC 38                     sub rsp, 0x38
007C7F84  48 8B D1                        mov rdx, rcx
007C7F87  48 8B 0D 9A 7A 73 00            mov rcx, qword ptr [rip + 0x737a9a]
007C7F8E  48 85 C9                        test rcx, rcx
007C7F91  74 11                           je 0x1407c7fa4
007C7F93  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007C7F99  45 33 C9                        xor r9d, r9d
007C7F9C  45 33 C0                        xor r8d, r8d
007C7F9F  E8 7C 47 C5 FF                  call 0x14041c720
007C7FA4  48 83 C4 38                     add rsp, 0x38
007C7FA8  C3                              ret
007C7FA9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_007C7F80(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    if (*(unsigned __int64 *)(v_rip + 7568026) != 0) {
        a4 = 0;
        a3 = 0;
        result = EtwWrite(*(unsigned __int64 *)(v_rip + 7568026), a1, a3, a4);
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_007C7F80(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    if (*(uint64_t *)(v_rip + 0x737A9A) != 0) {
        Arg4 = 0;
        Arg3 = 0;
        result = EtwWrite(*(uint64_t *)(v_rip + 0x737A9A), Arg1, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C7F80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C7F80[BB_007C7F80]
  bb_007C7F93[BB_007C7F93]
  bb_007C7FA4[BB_007C7FA4]
  bb_007C7FA9[BB_007C7FA9]
  bb_007C7F80 -->|branch| bb_007C7FA4
  bb_007C7F80 -->|fallthrough| bb_007C7F93
  bb_007C7F93 -->|flow| bb_007C7FA4
```
