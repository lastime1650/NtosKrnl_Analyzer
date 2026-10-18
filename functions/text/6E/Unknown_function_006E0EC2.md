# sub_006E0EC2

- RVA: `0x006E0EC2`–`0x006E0ED9` (길이 `23` bytes)
- VA: `0x00000001406E0EC2`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074100`
- 디코드: `6`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E0EC6` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E0ED4` → [sub_0030F26B + 0x15B](../30/Unknown_function_0030F26B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E0EC2  48 8D 4D 38                     lea rcx, [rbp + 0x38]
006E0EC6  E8 35 AE D1 FF                  call 0x1403fbd00
006E0ECB  49 8B 45 00                     mov rax, qword ptr [r13]
006E0ECF  48 85 C0                        test rax, rax
006E0ED2  75 EE                           jne 0x1406e0ec2
006E0ED4  E9 ED E4 C2 FF                  jmp 0x14030f3c6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E0EC2(void)
{
    __int64 result;

    result = KeYieldProcessorEx(v_rbp + 56, a2, a3, a4);
    if (*(unsigned __int64 *)(v_r13) != 0) goto loc_006E0EC2;
}
```

## 5. (Beta) C Style

```c
void sub_006E0EC2(void)
{
    int64_t result;

    result = KeYieldProcessorEx(local_rbp + 56, a2, a3, a4);
    if (*(uint64_t *)(local_r13) != 0) goto loc_006E0EC2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E0EC2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E0EC2[BB_006E0EC2]
  bb_006E0ED4[BB_006E0ED4]
  bb_006E0EC2 -->|branch| bb_006E0EC2
  bb_006E0EC2 -->|fallthrough| bb_006E0ED4
```
