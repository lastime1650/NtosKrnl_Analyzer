# itoa

- RVA: `0x004FF9A0`–`0x004FF9C9` (길이 `41` bytes)
- VA: `0x00000001404FF9A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FF9BA` → [xtoa](xtoa_function_004FF9D0.md) (function, `0x004FF9D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FF9A0  40 53                           push rbx
004FF9A2  48 83 EC 20                     sub rsp, 0x20
004FF9A6  45 33 C9                        xor r9d, r9d
004FF9A9  48 8B DA                        mov rbx, rdx
004FF9AC  41 83 F8 0A                     cmp r8d, 0xa
004FF9B0  75 08                           jne 0x1404ff9ba
004FF9B2  85 C9                           test ecx, ecx
004FF9B4  79 04                           jns 0x1404ff9ba
004FF9B6  45 8D 48 F7                     lea r9d, [r8 - 9]
004FF9BA  E8 11 00 00 00                  call 0x1404ff9d0
004FF9BF  48 8B C3                        mov rax, rbx
004FF9C2  48 83 C4 20                     add rsp, 0x20
004FF9C6  5B                              pop rbx
004FF9C7  C3                              ret
004FF9C8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall itoa(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a4 = 0;
    if (((unsigned int)(a3)) != 10) goto loc_004FF9BA;
    if (sign_flag) {
        a4 = a3 - 9;
    }
    result = xtoa(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return a2;
}
```

## 5. (Beta) C Style

```c
int64_t itoa(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg4 = 0;
    if (((uint32_t)(Arg3)) != 10) goto loc_004FF9BA;
    if (sign_flag) {
        Arg4 = Arg3 - 9;
    }
    result = xtoa(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (32);
    return Arg2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FF9A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FF9A0[BB_004FF9A0]
  bb_004FF9B2[BB_004FF9B2]
  bb_004FF9B6[BB_004FF9B6]
  bb_004FF9BA[BB_004FF9BA]
  bb_004FF9C8[BB_004FF9C8]
  bb_004FF9A0 -->|branch| bb_004FF9BA
  bb_004FF9A0 -->|fallthrough| bb_004FF9B2
  bb_004FF9B2 -->|branch| bb_004FF9BA
  bb_004FF9B2 -->|fallthrough| bb_004FF9B6
  bb_004FF9B6 -->|flow| bb_004FF9BA
```
