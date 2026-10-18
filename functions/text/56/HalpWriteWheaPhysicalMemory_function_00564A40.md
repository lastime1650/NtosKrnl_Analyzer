# HalpWriteWheaPhysicalMemory

- RVA: `0x00564A40`–`0x00564A5A` (길이 `26` bytes)
- VA: `0x0000000140564A40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00564A4F` → [HalpReadWriteWheaPhysicalMemory](HalpReadWriteWheaPhysicalMemory_function_005648B0.md) (function, `0x005648B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00564A40  48 83 EC 28                     sub rsp, 0x28
00564A44  4D 8B C8                        mov r9, r8
00564A47  44 8B C2                        mov r8d, edx
00564A4A  48 8B D1                        mov rdx, rcx
00564A4D  33 C9                           xor ecx, ecx
00564A4F  E8 5C FE FF FF                  call 0x1405648b0
00564A54  48 83 C4 28                     add rsp, 0x28
00564A58  C3                              ret
00564A59  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpWriteWheaPhysicalMemory(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = 0;
    result = HalpReadWriteWheaPhysicalMemory(a1, a1, (unsigned int)(a2), a3);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpWriteWheaPhysicalMemory(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = 0;
    result = HalpReadWriteWheaPhysicalMemory(Arg1, Arg1, (uint32_t)(Arg2), Arg3);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00564A40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00564A40[BB_00564A40]
  bb_00564A59[BB_00564A59]
```
