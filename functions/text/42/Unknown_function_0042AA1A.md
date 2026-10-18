# sub_0042AA1A

- RVA: `0x0042AA1A`–`0x0042AA5C` (길이 `66` bytes)
- VA: `0x000000014042AA1A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A1214`
- 디코드: `19`개 명령, `66/66` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0042AA33` → [sub_0042AA5C](Unknown_function_0042AA5C.md) (`tail-transfer`)
  - `0x0042AA5A` → [RtlAreBitsSetEx + 0x35](RtlAreBitsSetEx_function_0042A9C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0042AA1A  48 89 1C 24                     mov qword ptr [rsp], rbx
0042AA1E  49 8D 58 FF                     lea rbx, [r8 - 1]
0042AA22  48 03 DA                        add rbx, rdx
0042AA25  48 8B C3                        mov rax, rbx
0042AA28  48 C1 E8 06                     shr rax, 6
0042AA2C  4C 8D 1C C1                     lea r11, [rcx + rax*8]
0042AA30  4D 3B CB                        cmp r9, r11
0042AA33  75 27                           jne 0x14042aa5c
0042AA35  B9 40 00 00 00                  mov ecx, 0x40
0042AA3A  41 2A C8                        sub cl, r8b
0042AA3D  49 C7 C0 FF FF FF FF            mov r8, 0xffffffffffffffff
0042AA44  49 D3 E8                        shr r8, cl
0042AA47  48 8B CA                        mov rcx, rdx
0042AA4A  49 D3 E0                        shl r8, cl
0042AA4D  4D 23 D0                        and r10, r8
0042AA50  4D 3B D0                        cmp r10, r8
0042AA53  0F 94 C0                        sete al
0042AA56  48 8B 1C 24                     mov rbx, qword ptr [rsp]
0042AA5A  EB 99                           jmp 0x14042a9f5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0042AA1A(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    unsigned __int64 v_stack_p0;

    v_stack_p0 = v_rbx;
    v_rbx = (a3 - 1) + (a2);
    result = (v_rbx) >> (6);
    a1 = (unsigned __int8)((64) - ((unsigned __int8)(a3)));
    a3 = (-1) >> ((unsigned __int8)(a1));
    a3 = (a3) << ((unsigned __int8)(a2));
    v_r10 = (v_r10) & (a3);
    result = (v_r10 == a3) ? 1 : 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0042AA1A(void *Arg1, int64_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    uint64_t v_stack_p0;

    v_stack_p0 = local_rbx;
    local_rbx = (Arg3 - 1) + (Arg2);
    result = (local_rbx) >> (6);
    Arg1 = (uint8_t)((64) - ((uint8_t)(Arg3)));
    Arg3 = (-1) >> ((uint8_t)(Arg1));
    Arg3 = (Arg3) << ((uint8_t)(Arg2));
    local_r10 = (local_r10) & (Arg3);
    result = (local_r10 == Arg3) ? 1 : 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg3` | `- 0x1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042AA1A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042AA1A[BB_0042AA1A]
  bb_0042AA35[BB_0042AA35]
  bb_0042AA1A -->|fallthrough| bb_0042AA35
```
