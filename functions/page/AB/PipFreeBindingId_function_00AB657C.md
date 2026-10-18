# PipFreeBindingId

- RVA: `0x00AB657C`–`0x00AB65A2` (길이 `38` bytes)
- VA: `0x0000000140AB657C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AB6589` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00AB6596` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PipDeleteDependencyNode](../6F/PipDeleteDependencyNode_function_006FE670.md) at `0x006FE69F`
- [PipDeleteBindingId](../72/PipDeleteBindingId_function_00727BFC.md) at `0x00727C58`
- [PipDeleteBindingIds](PipDeleteBindingIds_function_00AB6538.md) at `0x00AB6560`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AB6596` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB657C  40 53                           push rbx
00AB657E  48 83 EC 20                     sub rsp, 0x20
00AB6582  48 8B D9                        mov rbx, rcx
00AB6585  48 83 C1 10                     add rcx, 0x10
00AB6589  E8 72 A2 F0 FF                  call 0x1409c0800
00AB658E  BA 50 6E 70 53                  mov edx, 0x53706e50
00AB6593  48 8B CB                        mov rcx, rbx
00AB6596  E8 D5 C2 0C 00                  call 0x140b82870
00AB659B  48 83 C4 20                     add rsp, 0x20
00AB659F  5B                              pop rbx
00AB65A0  C3                              ret
00AB65A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipFreeBindingId(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (16);
    result = RtlFreeAnsiString(a1, a2, a3, a4);
    result = ExFreePoolWithTag(a1, (unsigned int)(0x53706E50ULL), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipFreeBindingId(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (16);
    result = RtlFreeAnsiString(Arg1, a2, a3, a4);
    result = ExFreePoolWithTag(Arg1, (uint32_t)(0x53706E50ULL), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB657C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB657C[BB_00AB657C]
  bb_00AB65A1[BB_00AB65A1]
```
