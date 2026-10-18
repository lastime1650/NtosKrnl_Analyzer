# ObAssignObjectSecurityDescriptor

- RVA: `0x009A7310`–`0x009A732C` (길이 `28` bytes)
- VA: `0x00000001409A7310`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009CABC`
- 디코드: `8`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [WmipSecurityMethod](WmipSecurityMethod_function_009A71F0.md) at `0x009A724E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x009A7322` → [sub_009A76D2](Unknown_function_009A76D2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009A7310  48 8B C4                        mov rax, rsp
009A7313  48 89 48 08                     mov qword ptr [rax + 8], rcx
009A7317  55                              push rbp
009A7318  48 83 EC 50                     sub rsp, 0x50
009A731C  48 8B EA                        mov rbp, rdx
009A731F  48 85 D2                        test rdx, rdx
009A7322  0F 84 AA 03 00 00               je 0x1409a76d2
009A7328  0F BF 4A 02                     movsx ecx, word ptr [rdx + 2]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObAssignObjectSecurityDescriptor(__int64 a1, __int64 a2)
{
    __int64 v_rsp;

    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    return v_rsp;
}
```

## 5. (Beta) C Style

```c
int64_t ObAssignObjectSecurityDescriptor(int64_t Arg1, int64_t Arg2)
{
    int64_t local_rsp;

    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    return local_rsp;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A7310&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A7310[BB_009A7310]
  bb_009A7328[BB_009A7328]
  bb_009A7310 -->|fallthrough| bb_009A7328
```
