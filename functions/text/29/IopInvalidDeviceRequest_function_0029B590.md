# IopInvalidDeviceRequest

- RVA: `0x0029B590`–`0x0029B5B0` (길이 `32` bytes)
- VA: `0x000000014029B590`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0029B5A0` → [IofCompleteRequest](IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)

### Direct callers
- [IofCallDriver](IofCallDriver_function_0029B4B0.md) at `0x0029B524`
- [IopfCallDriver](IopfCallDriver_function_0029C474.md) at `0x0029C4D1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0029B590  48 83 EC 28                     sub rsp, 0x28
0029B594  48 8B CA                        mov rcx, rdx
0029B597  C7 42 30 10 00 00 C0            mov dword ptr [rdx + 0x30], 0xc0000010
0029B59E  33 D2                           xor edx, edx
0029B5A0  E8 1B 00 00 00                  call 0x14029b5c0
0029B5A5  B8 10 00 00 C0                  mov eax, 0xc0000010
0029B5AA  48 83 C4 28                     add rsp, 0x28
0029B5AE  C3                              ret
0029B5AF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopInvalidDeviceRequest(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned int *)(a2 + 48) = 0xC0000010ULL;
    a2 = 0;
    result = IofCompleteRequest(a2, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC0000010ULL);
}
```

## 5. (Beta) C Style

```c
int64_t IopInvalidDeviceRequest(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint32_t *)(arg2 + 0x30) = 0xC0000010ULL;
    Arg2 = 0;
    result = IofCompleteRequest(Arg2, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC0000010ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0029B590&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0029B590[BB_0029B590]
  bb_0029B5AF[BB_0029B5AF]
```
